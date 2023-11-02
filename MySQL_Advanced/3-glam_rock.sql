-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, SUB(split, formed) as lifespan
FROM glam_rock
WHERE style = 'Glam rock'

