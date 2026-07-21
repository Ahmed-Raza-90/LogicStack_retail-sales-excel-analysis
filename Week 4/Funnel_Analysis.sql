SELECT COUNT(*) FROM client_site;

SELECT COUNT(*) AS total_rows
FROM client_site;

SELECT COUNT(DISTINCT user_id) AS unique_users
FROM client_site;

SELECT COUNT(DISTINCT session_id) AS unique_sessions
FROM client_site;

SELECT DISTINCT event
FROM client_site;


SELECT
    event,
    COUNT(*) AS total_events
FROM client_site
GROUP BY event
ORDER BY total_events DESC;


SELECT DISTINCT event
FROM client_site
ORDER BY event;



Task 2: Funnel Stage Analysis 
1. Count total events by type 

SELECT
    event,
    COUNT(*) AS total_events
FROM client_site
GROUP BY event
ORDER BY total_events DESC;

2. Count users per event type 
SELECT
    event,
    COUNT(DISTINCT user_id) AS total_users
FROM client_site
GROUP BY event
ORDER BY total_users DESC;

3. Find conversion from view → purchase
SELECT
    COUNT(DISTINCT CASE WHEN "event" = 'Browse' THEN user_id END) AS browse_users,
    COUNT(DISTINCT CASE WHEN "event" = 'Purchase' THEN user_id END) AS purchase_users,
    ROUND(
        COUNT(DISTINCT CASE WHEN "event" = 'Purchase' THEN user_id END)::numeric
        /
        NULLIF(COUNT(DISTINCT CASE WHEN "event" = 'Browse' THEN user_id END), 0)
        * 100,
        2
    ) AS conversion_rate
FROM public.client_site;

--Task 3: Revenue Analysis
--Total Revenue
SELECT
    SUM(revenue) AS total_revenue
FROM client_site;

--Revenue by Region
SELECT
    region,
    SUM(revenue) AS revenue
FROM client_site
GROUP BY region
ORDER BY revenue DESC;


-- Revenue by Channel
SELECT
    channel,
    SUM(revenue) AS revenue
FROM client_site
GROUP BY channel
ORDER BY revenue DESC;

-- Revenue by Device
SELECT
    device,
    SUM(revenue) AS revenue
FROM client_site
GROUP BY device
ORDER BY revenue DESC;


-- Task 4: Business Insights
-- Top 5 Users by Revenue
SELECT
    user_id,
    SUM(revenue) AS total_revenue
FROM client_site
GROUP BY user_id
ORDER BY total_revenue DESC
LIMIT 5;


-- Best Performing Channel
SELECT
    channel,
    SUM(revenue) AS revenue
FROM client_site
GROUP BY channel
ORDER BY revenue DESC
LIMIT 1;

-- Highest Revenue Region
SELECT
    region,
    SUM(revenue) AS revenue
FROM client_site
GROUP BY region
ORDER BY revenue DESC
LIMIT 1;


-- Device with Highest Purchase Count
SELECT
    device,
    COUNT(*) AS purchases
FROM client_site
WHERE event = 'Purchase'
GROUP BY device
ORDER BY purchases DESC;


-- Task 5: Drop-off Analysis
-- Funnel Counts
SELECT
    event,
    COUNT(DISTINCT user_id) AS users
FROM client_site
GROUP BY event
ORDER BY
CASE event
    WHEN 'Browse' THEN 1
    WHEN 'Add to Cart' THEN 2
    WHEN 'Checkout' THEN 3
    WHEN 'Purchase' THEN 4
END;


-- Biggest Drop-off Between Funnel Stages
WITH funnel AS (
SELECT
event,
COUNT(DISTINCT user_id) AS users
FROM client_site
GROUP BY event
)

SELECT *
FROM funnel;


-- Lowest Conversion Event
SELECT
event,
COUNT(*) AS total_events
FROM client_site
GROUP BY event
ORDER BY total_events ASC
LIMIT 1;