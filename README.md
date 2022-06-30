# 🎉 IPv4 & IPv6 WHOIS Database



# 🔗 Website: [ip.js0.ch](https://ip.js0.ch)

# ℹ️ Info
This project covers all IPv4 and IPv6 addresses worldwide and outputs 23 different criteria over this IP. The database was kept as minimal as possible, so that it can be operated performantly even on servers without much computing power. The database is usually updated about once a month.

I also provide a free, unlimited API to test the database. It can be found on the project website ip.js0.ch.
<br><br><br>
Sample SQL Query (Used in API):<br>
(Replace {{IP IN DECIMAL}} with your IP in decimal Format)
```    
SELECT (ip.decimal_end-ip.decimal_start) AS ip_range,
       ip.ip_start AS ip_rangeStart,
       ip.ip_end AS ip_rangeEnd,
       ip.lon AS loc_lon,
       ip.lat AS loc_lat,
       ip.region AS loc_region,
       ip.city AS loc_city,
       ip.zip AS loc_zip,
       ip.asn AS asn_id,
       asn.name AS asn_name,
       asn.type AS asn_type,
       asn.isp AS asn_isp,
       ip.countryCode AS loc_countryCode,
       country.countryCode3 AS loc_countryCode3,
       country.countryCode AS loc_countryCodeDecimal,
       country.region AS loc_countryRegion,
       country.regionCode AS loc_countryRegionCode,
       country.subregion AS loc_countrySubRegion,
       country.subregionCode AS loc_countrySubRegionCode,
       country.language AS loc_language,
       country.currencies AS loc_currencies,
       country.callingCode AS loc_callingCode,
       country.name AS loc_countryName
FROM ip
LEFT JOIN asn ON ip.asn = asn.id
LEFT JOIN country ON ip.countryCode = country.id
WHERE ip.decimal_start {{IP IN DECIMAL}}
ORDER BY ip.decimal_start DESC
LIMIT 1
```


# 🧱 Structure
![table](https://user-images.githubusercontent.com/76683226/176740929-2ee938ef-e895-4f65-aa68-f8092a0fac95.png)

# 📥 Download

| File | Link 1 | Link 2 |
|------|-------|--------|
| <b>SQL Database Dump</b> | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/database-dump.sql) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/database-dump.sql) |
| <b>CSV Combined</b> | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/csv/combined.csv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/csv/combined.csv) |
| CSV IP | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/csv/ip.csv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/csv/ip.csv) |
| CSV ASN | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/csv/asn.csv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/csv/asn.csv) |
| CSV Country | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/csv/country.csv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/csv/country.csv) |
| <b>TSV Combined</b> | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/tsv/combined.tsv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/tsv/combined.tsv) |
| TSV IP | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/tsv/ip.tsv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/tsv/ip.tsv) |
| TSV ASN | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/tsv/asn.tsv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/tsv/asn.tsv) |
| TSV Country | [GitHub](https://github.com/saschazesiger/IP-WHOIS-Database/blob/main/tsv/country.tsv) | [RAW](https://media.githubusercontent.com/media/saschazesiger/IP-WHOIS-Database/main/tsv/country.tsv) |


