CREATE DATABASE marketing_performance_analysis;
USE marketing_performance_analysis;

-- Validate imported records
SELECT COUNT(*) AS total_campaigns
FROM marketing_campaigns;

-- Preview campaign data
SELECT *
FROM marketing_campaigns
LIMIT 10;

-- Check table schema
DESCRIBE marketing_campaigns;

-- View campaign date range
SELECT
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM marketing_campaigns;

-- Count campaigns by platform
SELECT
    platform,
    COUNT(*) AS total_campaigns
FROM marketing_campaigns
GROUP BY platform
ORDER BY total_campaigns DESC;


-- =====================================================
-- BUSINESS ANALYSIS
-- =====================================================


-- Average revenue by platform
SELECT
    platform,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY platform
ORDER BY avg_revenue DESC;


-- Average advertising spend by platform
SELECT
    platform,
    ROUND(AVG(spend), 2) AS avg_spend
FROM marketing_campaigns
GROUP BY platform
ORDER BY avg_spend DESC;

-- Average ROAS by platform
SELECT
    platform,
    ROUND(AVG(ROAS), 2) AS avg_roas
FROM marketing_campaigns
GROUP BY platform
ORDER BY avg_roas DESC;

-- Average CTR by platform
SELECT
    platform,
    ROUND(AVG(CTR), 2) AS avg_ctr
FROM marketing_campaigns
GROUP BY platform
ORDER BY avg_ctr DESC;

-- Average revenue by campaign objective
SELECT
    objective,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY objective
ORDER BY avg_revenue DESC;

-- Average revenue by country
SELECT
    country,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY country
ORDER BY avg_revenue DESC;

-- Average revenue by funnel stage
SELECT
    funnel_stage,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY funnel_stage
ORDER BY avg_revenue DESC;

-- Average revenue by account type
SELECT
    account_type,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY account_type
ORDER BY avg_revenue DESC;

-- Average revenue by campaign theme
SELECT
    theme,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY theme
ORDER BY avg_revenue DESC;

-- Monthly revenue trend
SELECT
    year,
    month_name,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY year, month, month_name
ORDER BY year, month;

-- Top 10 campaigns by revenue
SELECT
    campaign_name,
    platform,
    ROUND(revenue, 2) AS revenue
FROM marketing_campaigns
ORDER BY revenue DESC
LIMIT 10;

-- Top 10 campaigns by ROAS
SELECT
    campaign_name,
    platform,
    ROUND(ROAS, 2) AS roas
FROM marketing_campaigns
ORDER BY ROAS DESC
LIMIT 10;

-- Platform performance summary
SELECT
    platform,
    COUNT(*) AS total_campaigns,
    ROUND(AVG(spend), 2) AS avg_spend,
    ROUND(AVG(revenue), 2) AS avg_revenue,
    ROUND(AVG(ROAS), 2) AS avg_roas
FROM marketing_campaigns
GROUP BY platform
ORDER BY avg_revenue DESC;

-- Revenue by season
SELECT
    season,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY season
ORDER BY avg_revenue DESC;

-- Weekend vs weekday performance
SELECT
    `is_weekend (text)` AS day_type,
    ROUND(AVG(revenue), 2) AS avg_revenue,
    ROUND(AVG(CTR), 2) AS avg_ctr,
    ROUND(AVG(ROAS), 2) AS avg_roas
FROM marketing_campaigns
GROUP BY `is_weekend (text)`
ORDER BY avg_revenue DESC;

-- =====================================================
-- ADVANCED SQL ANALYSIS
-- =====================================================


-- Rank platforms by average revenue
SELECT
    platform,
    ROUND(AVG(revenue), 2) AS avg_revenue,
    RANK() OVER (
        ORDER BY AVG(revenue) DESC
    ) AS revenue_rank
FROM marketing_campaigns
GROUP BY platform;

-- Rank countries by average revenue
SELECT
    country,
    ROUND(AVG(revenue), 2) AS avg_revenue,
    DENSE_RANK() OVER (
        ORDER BY AVG(revenue) DESC
    ) AS revenue_rank
FROM marketing_campaigns
GROUP BY country;

-- Compare platform performance with the overall average revenue
WITH platform_revenue AS
(
    SELECT
        platform,
        ROUND(AVG(revenue),2) AS avg_revenue
    FROM marketing_campaigns
    GROUP BY platform
)

SELECT
    platform,
    avg_revenue,
    (
        SELECT ROUND(AVG(revenue),2)
        FROM marketing_campaigns
    ) AS overall_average
FROM platform_revenue
ORDER BY avg_revenue DESC;

-- Classify campaigns based on revenue
SELECT
    campaign_name,
    revenue,

    CASE

        WHEN revenue >= 5000 THEN 'High Performer'

        WHEN revenue >= 1000 THEN 'Medium Performer'

        ELSE 'Low Performer'

    END AS performance_category

FROM marketing_campaigns;


-- Top campaign by revenue within each platform
WITH ranked_campaigns AS
(
    SELECT
        platform,
        campaign_name,
        revenue,

        ROW_NUMBER() OVER
        (
            PARTITION BY platform
            ORDER BY revenue DESC
        ) AS ranking

    FROM marketing_campaigns
)

SELECT
    platform,
    campaign_name,
    ROUND(revenue,2) AS revenue
FROM ranked_campaigns
WHERE ranking = 1;


-- =====================================================
-- ADVANCED BUSINESS INSIGHTS
-- =====================================================

-- Platforms performing above the overall average revenue
SELECT
    platform,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY platform
HAVING AVG(revenue) >
(
    SELECT AVG(revenue)
    FROM marketing_campaigns
)
ORDER BY avg_revenue DESC;

-- Campaign objectives with above-average ROAS
SELECT
    objective,
    ROUND(AVG(ROAS), 2) AS avg_roas
FROM marketing_campaigns
GROUP BY objective
HAVING AVG(ROAS) >
(
    SELECT AVG(ROAS)
    FROM marketing_campaigns
)
ORDER BY avg_roas DESC;


-- Total revenue generated by each platform
SELECT
    platform,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM marketing_campaigns
GROUP BY platform
ORDER BY total_revenue DESC;

-- Total advertising spend by platform
SELECT
    platform,
    ROUND(SUM(spend), 2) AS total_spend
FROM marketing_campaigns
GROUP BY platform
ORDER BY total_spend DESC;

-- Overall conversion rate by platform
SELECT
    platform,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    ROUND(
        (SUM(conversions) * 100.0) / NULLIF(SUM(clicks), 0),
        2
    ) AS conversion_rate
FROM marketing_campaigns
GROUP BY platform
ORDER BY conversion_rate DESC;

-- High-performing campaigns based on ROAS

SELECT
    campaign_name,
    platform,
    ROUND(spend,2) AS spend,
    ROUND(revenue,2) AS revenue,
    ROUND(ROAS,2) AS roas
FROM marketing_campaigns
WHERE ROAS >
(
    SELECT AVG(ROAS)
    FROM marketing_campaigns
)
ORDER BY ROAS DESC;

-- Campaigns generating revenue below the overall average
SELECT
    campaign_name,
    platform,
    ROUND(revenue,2) AS revenue
FROM marketing_campaigns
WHERE revenue <
(
    SELECT AVG(revenue)
    FROM marketing_campaigns
)
ORDER BY revenue;

-- Revenue generated per unit of advertising spend
SELECT
    platform,
    ROUND(
        SUM(revenue) / SUM(spend),
        2
    ) AS revenue_per_spend
FROM marketing_campaigns
GROUP BY platform
ORDER BY revenue_per_spend DESC;

-- Top five countries by total revenue
SELECT
    country,
    ROUND(SUM(revenue),2) AS total_revenue
FROM marketing_campaigns
GROUP BY country
ORDER BY total_revenue DESC
LIMIT 5;


-- Revenue contribution by platform
SELECT
    platform,
    ROUND(SUM(revenue),2) AS total_revenue,
    ROUND(
        SUM(revenue) * 100 /
        (
            SELECT SUM(revenue)
            FROM marketing_campaigns
        ),
        2
    ) AS revenue_share_percent
FROM marketing_campaigns
GROUP BY platform
ORDER BY revenue_share_percent DESC;


-- Best-performing theme by platform based on average revenue
WITH theme_performance AS (
    SELECT
        platform,
        theme,
        ROUND(AVG(revenue), 2) AS avg_revenue,
        RANK() OVER (
            PARTITION BY platform
            ORDER BY AVG(revenue) DESC
        ) AS revenue_rank
    FROM marketing_campaigns
    GROUP BY platform, theme
)

SELECT
    platform,
    theme,
    avg_revenue
FROM theme_performance
WHERE revenue_rank = 1
ORDER BY avg_revenue DESC;


-- Best-performing season by platform
WITH seasonal_performance AS (
    SELECT
        platform,
        season,
        ROUND(AVG(revenue), 2) AS avg_revenue,
        RANK() OVER (
            PARTITION BY platform
            ORDER BY AVG(revenue) DESC
        ) AS revenue_rank
    FROM marketing_campaigns
    GROUP BY platform, season
)

SELECT
    platform,
    season,
    avg_revenue
FROM seasonal_performance
WHERE revenue_rank = 1
ORDER BY avg_revenue DESC;


-- Highest-performing objective by platform
WITH objective_performance AS (
    SELECT
        platform,
        objective,
        ROUND(AVG(ROAS), 2) AS avg_roas,
        RANK() OVER (
            PARTITION BY platform
            ORDER BY AVG(ROAS) DESC
        ) AS roas_rank
    FROM marketing_campaigns
    GROUP BY platform, objective
)

SELECT
    platform,
    objective,
    avg_roas
FROM objective_performance
WHERE roas_rank = 1
ORDER BY avg_roas DESC;

-- Platforms with above-average revenue
SELECT
    platform,
    ROUND(AVG(revenue), 2) AS avg_revenue
FROM marketing_campaigns
GROUP BY platform
HAVING AVG(revenue) >
(
    SELECT AVG(revenue)
    FROM marketing_campaigns
)
ORDER BY avg_revenue DESC;


-- Compare platform ROAS with the overall average
SELECT
    platform,
    ROUND(AVG(roas), 2) AS avg_roas,
    ROUND(
        AVG(roas) -
        (SELECT AVG(roas) FROM marketing_campaigns),
        2
    ) AS difference_from_average
FROM marketing_campaigns
GROUP BY platform
ORDER BY avg_roas DESC;

-- Highest revenue-generating country for each platform
WITH country_revenue AS
(
    SELECT
        platform,
        country,
        ROUND(SUM(revenue), 2) AS total_revenue,
        ROW_NUMBER() OVER
        (
            PARTITION BY platform
            ORDER BY SUM(revenue) DESC
        ) AS revenue_rank
    FROM marketing_campaigns
    GROUP BY platform, country
)

SELECT
    platform,
    country,
    total_revenue
FROM country_revenue
WHERE revenue_rank = 1
ORDER BY total_revenue DESC;



-- =====================================================
-- SQL VIEWS FOR POWER BI
-- =====================================================

-- Create a reusable platform performance view

CREATE OR REPLACE VIEW vw_platform_performance AS

SELECT
    platform,
    COUNT(*) AS total_campaigns,
    ROUND(SUM(spend),2) AS total_spend,
    ROUND(SUM(revenue),2) AS total_revenue,
    ROUND(AVG(CTR),2) AS avg_ctr,
    ROUND(AVG(ROAS),2) AS avg_roas,
    ROUND(
        SUM(conversions) * 100.0 /
        NULLIF(SUM(clicks),0),
        2
    ) AS conversion_rate
FROM marketing_campaigns
GROUP BY platform;

-- Create a reusable country performance view
CREATE OR REPLACE VIEW vw_country_performance AS

SELECT
    country,
    COUNT(*) AS total_campaigns,
    ROUND(SUM(spend),2) AS total_spend,
    ROUND(SUM(revenue),2) AS total_revenue,
    ROUND(AVG(ROAS),2) AS avg_roas
FROM marketing_campaigns
GROUP BY country;

-- Create a reusable monthly performance view
CREATE OR REPLACE VIEW vw_monthly_performance AS

SELECT
    year,
    month,
    month_name,
    ROUND(SUM(spend),2) AS total_spend,
    ROUND(SUM(revenue),2) AS total_revenue,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    ROUND(AVG(CTR),2) AS avg_ctr,
    ROUND(AVG(ROAS),2) AS avg_roas
FROM marketing_campaigns
GROUP BY
    year,
    month,
    month_name;
    
-- Create a reusable campaign performance view
CREATE OR REPLACE VIEW vw_campaign_performance AS

SELECT
    campaign_name,
    platform,
    country,
    objective,
    theme,
    spend,
    revenue,
    CTR,
    ROAS,

    CASE
        WHEN revenue >= 5000 THEN 'High Performer'
        WHEN revenue >= 1000 THEN 'Medium Performer'
        ELSE 'Low Performer'
    END AS performance_category

FROM marketing_campaigns;

-- Create a reusable executive dashboard view
CREATE OR REPLACE VIEW vw_executive_dashboard AS

SELECT
    platform,

    ROUND(SUM(spend),2) AS total_spend,

    ROUND(SUM(revenue),2) AS total_revenue,

    ROUND(
        SUM(revenue) /
        NULLIF(SUM(spend),0),
        2
    ) AS revenue_per_spend,

    ROUND(
        SUM(revenue) * 100 /
        (
            SELECT SUM(revenue)
            FROM marketing_campaigns
        ),
        2
    ) AS revenue_share_percent,

    ROUND(
        SUM(conversions) * 100.0 /
        NULLIF(SUM(clicks),0),
        2
    ) AS conversion_rate

FROM marketing_campaigns
GROUP BY platform;

SELECT * FROM vw_platform_performance;
SELECT * FROM vw_country_performance;
SELECT * FROM vw_monthly_performance;
SELECT * FROM vw_campaign_performance;
SELECT * FROM vw_executive_dashboard;