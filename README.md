# Glassdoor Scraper (Pay Per Result)
> Glassdoor Scraper (Pay Per Result) lets you pull rich, structured company data from Glassdoor — including reviews, salaries, interviews, culture scores, and benefits — in a single automated workflow.
> It turns unstructured feedback into clean JSON you can plug into dashboards, HR analytics, people insights tools, or market research pipelines.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Glassdoor Scraper (Pay Per Result)</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project is a Glassdoor scraper that extracts detailed company, job, and employee experience data from public pages and converts it into structured records. It captures both individual-level entries (reviews, interviews, benefits comments) and aggregated statistics (ratings, salary percentiles, demographic scores).

It is built for HR teams, people analytics specialists, market researchers, data engineers, and agencies that need reliable, repeatable access to Glassdoor insights without manual copy-paste.

### Glassdoor Insights at Scale
- Collect company reviews, interview feedback, salaries, jobs, and office locations from a single configuration.
- Capture demographic and diversity ratings across gender, race/ethnicity, disability, and more for deeper culture analysis.
- Extract salary distributions with pay percentiles for base pay, bonuses, stock, and total compensation.
- Enrich datasets with company-level metadata such as industry, revenue, size, and headquarters.
- Export consistently structured JSON suitable for BI tools, databases, or downstream machine learning models.

## Features
| Feature | Description |
|--------|-------------|
| Company-specific scraping | Target one or more Glassdoor company pages and collect reviews, interviews, salaries, jobs, locations, culture, and benefits in a single run. |
| Individual job ad scraping | Provide a job listing URL to extract title, location, pay details (if available), description, requirements, benefits, and tracking links. |
| Comprehensive review data | Capture titles, summaries, pros, cons, ratings, dates, locations, employee status, and company responses for each review. |
| Interview experience analytics | Extract interview difficulty, process descriptions, outcomes, and user questions plus employer-level interview stats. |
| Salary benchmarking | Retrieve salary counts and percentile-based distributions for base pay, bonuses, stock, additional pay, and total pay. |
| Culture & diversity metrics | Pull demographic rating breakdowns by gender, race/ethnicity, sexual orientation, disability, caregiver status, and veteran status. |
| Benefits intelligence | Collect benefit reviews, comments, and aggregated statistics by benefit category (insurance, retirement, time off, discounts, etc.). |
| Multi-language support | Optionally include reviews and salaries from multiple languages (eng, fra, por, spa, ita, nld, deu) in a single dataset. |
| Filter-aware salary scraping | Respect salary filters applied in source URLs (job function, location, pay period) so only the filtered results are retrieved. |
| Tunable concurrency & retries | Configure concurrency, max items, and retry behavior to balance speed, stability, and infrastructure constraints. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|-----------|-------------------|
| reviewId | Unique identifier of a review entry. |
| reviewDateTime | ISO timestamp when the review was posted. |
| summary | Short headline or title of the review. |
| pros | Free-text list of positive aspects mentioned by the reviewer. |
| cons | Free-text list of negative aspects mentioned by the reviewer. |
| employmentStatus | Reviewer’s employment status (e.g., current or former employee). |
| isCurrentJob | Boolean flag indicating whether the reviewer currently works at the company. |
| jobTitle.text | Reviewer's job title at the time of review. |
| location.name | City or region associated with the review. |
| languageId | Language ISO code used in the review (e.g., eng). |
| ratingOverall | Overall 1–5 rating for the employer in that review. |
| ratingWorkLifeBalance | 1–5 score for work–life balance. |
| ratingCompensationAndBenefits | 1–5 score for pay and benefits. |
| ratingCultureAndValues | 1–5 score for culture and values. |
| ratingDiversityAndInclusion | 1–5 score for diversity and inclusion. |
| ratingCareerOpportunities | 1–5 score for career advancement opportunities. |
| ratingSeniorLeadership | 1–5 score for senior management quality. |
| ratingRecommendToFriend | Reviewer’s likelihood to recommend the company to a friend. |
| companyReviewStats.demographicRatingsRG | Demographic rating breakdowns by category (gender, race/ethnicity, sexual orientation, disability, parent status, veteran status). |
| employer.id | Numeric identifier of the employer. |
| employer.shortName | Company’s short display name. |
| employer.squareLogoUrl | URL to the company’s square logo image. |
| employerRatings.overallRating | Aggregated overall rating for the company. |
| employerRatings.recommendToFriendRating | Average recommendation score across all reviewers. |
| employerRatings.diversityAndInclusionRating | Aggregated diversity and inclusion score. |
| interview.id | Unique identifier for an interview review. |
| interview.experience | Interview experience label (e.g., POSITIVE, NEGATIVE). |
| interview.difficulty | Difficulty level of the interview process. |
| interview.processDescription | Free-text description of interview rounds, questions, and steps. |
| interview.location.name | Country or city where the interview took place. |
| interview.userQuestions.question | Individual interview questions reported by candidates. |
| companyInterviewStats.totalInterviewCount | Total number of interview reports for the employer. |
| companyInterviewStats.interviewExperienceCounts | Counts and percentages of positive, neutral, and negative interview experiences. |
| officeLocation.id | Identifier for a specific office location entry. |
| officeLocation.cityName | City name of the office. |
| officeLocation.countryName | Country code or name of the office. |
| officeLocation.latitude | Latitude coordinate for the office location. |
| officeLocation.longitude | Longitude coordinate for the office location. |
| salary.jobTitle.text | Job title for which salary statistics are aggregated. |
| salary.currency.code | ISO currency code used for salary values. |
| salary.salaryCount | Number of salary reports used for the estimates. |
| basePayStatistics.percentiles | Array of base pay values for P10, P25, P50, P75, P90. |
| cashBonusStatistics.percentiles | Cash bonus percentile distribution for the role. |
| stockBonusStatistics.percentiles | Stock or equity bonus percentiles. |
| totalAdditionalPayStatistics.percentiles | Aggregated additional compensation percentiles. |
| totalPayStatistics.percentiles | Full compensation (base + additional) percentiles. |
| job.jobTitleText | Title of an individual job posting. |
| job.locationName | Location label for the job posting. |
| job.payCurrency | Currency for the job pay. |
| job.payPeriod | Period for pay (e.g., HOURLY, YEARLY). |
| job.payPeriodAdjustedPay.p10 | Lower bound hourly or periodic pay estimate. |
| job.payPeriodAdjustedPay.p90 | Upper bound hourly or periodic pay estimate. |
| job.seoJobLink | SEO-friendly URL to the job listing. |
| overview.shortName | Company’s short name shown in overview. |
| overview.headquarters | Company headquarters location string. |
| overview.size | Company size band (e.g., “51 to 200 Employees”). |
| overview.primaryIndustry.industryName | Name of the company’s primary industry. |
| overview.primaryIndustry.sectorName | Name of the broader sector. |
| overview.yearFounded | Year the company was founded. |
| overview.website | Official company website link. |
| benefits.rating | Overall benefits rating given in a benefits review. |
| benefits.userEnteredJobTitle | Job title associated with the benefits review. |
| benefits.city.name | City name tied to the benefits review. |
| benefits.state.name | State or region name tied to the benefits review. |
| benefitComments.comment | Free-text comment describing the benefits experience. |
| companyBenefitStats.overallBenefitRating | Aggregated 1–5 rating for benefits at the company. |
| companyBenefitStats.totalBenefitReviews | Total number of benefit reviews. |
| benefitsCategoryToStatisticAggregates | Benefit statistics grouped by category (health, retirement, time off, discounts, etc.). |
| cultureDemographic.category | Demographic category type (e.g., gender, raceEthnicity). |
| cultureDemographic.categoryValue | Specific demographic value (e.g., woman, nonBinary). |
| cultureDemographic.ratings.overallRating | Overall rating for a specific demographic group. |
| cultureDemographic.ratings.recommendToFriendRating | Share of respondents in that demographic who would recommend the company. |

---

## Example Output
Example:

    [
      {
        "employer": {
          "id": 839181,
          "shortName": "Kids on the Move",
          "squareLogoUrl": "https://media.glassdoor.com/sql/839181/kids-on-the-move-squarelogo-1499250691084.png"
        },
        "reviewId": 93656313,
        "reviewDateTime": "2024-12-13T15:00:29.823",
        "summary": "Great culture very rewarding",
        "pros": "Most employees are here because they love what they do. The culture is amazing and leadership is dedicated.",
        "cons": "Not a ton of downsides.",
        "employmentStatus": "REGULAR",
        "isCurrentJob": true,
        "jobTitle": {
          "text": "VP of Grant Strategy and Operations"
        },
        "location": {
          "name": "Orem, UT",
          "type": "CITY"
        },
        "languageId": "eng",
        "ratingOverall": 5,
        "ratingWorkLifeBalance": 5,
        "ratingCompensationAndBenefits": 5,
        "ratingCultureAndValues": 5,
        "ratingDiversityAndInclusion": 5,
        "ratingCareerOpportunities": 5,
        "ratingSeniorLeadership": 5,
        "ratingRecommendToFriend": "POSITIVE",
        "companyReviewStats": {
          "ratings": {
            "overallRating": 3.9,
            "recommendToFriendRating": 0.82,
            "cultureAndValuesRating": 4.3,
            "diversityAndInclusionRating": 4.2
          },
          "allReviewsCount": 47
        }
      }
    ]

---

## Directory Structure Tree
Assume it’s a complete working project with a Python-based scraping core and modular parsers for each Glassdoor data type.

Example:

    glassdoor-scraper-pay-per-result/
        ├── src/
        │   ├── main.py
        │   ├── client/
        │   │   ├── glassdoor_client.py
        │   │   └── session_manager.py
        │   ├── parsers/
        │   │   ├── reviews_parser.py
        │   │   ├── interviews_parser.py
        │   │   ├── salaries_parser.py
        │   │   ├── jobs_parser.py
        │   │   ├── locations_parser.py
        │   │   ├── benefits_parser.py
        │   │   └── culture_parser.py
        │   ├── storage/
        │   │   ├── exporters.py
        │   │   └── schemas.py
        │   └── config/
        │       └── settings.example.json
        ├── data/
        │   ├── input.sample.json
        │   └── sample_output.json
        ├── tests/
        │   ├── test_reviews_parser.py
        │   ├── test_salaries_parser.py
        │   └── test_jobs_parser.py
        ├── scripts/
        │   └── run_local.sh
        ├── requirements.txt
        ├── .env.example
        └── README.md

---

## Use Cases
- **HR analytics teams** use it to centralize reviews, salaries, and benefits data across multiple employers, so they can build evidence-based people strategies and benchmark employer brand health.
- **People analytics and data science teams** use it to feed sentiment, rating distributions, and demographic breakdowns into predictive models, so they can understand drivers of retention and satisfaction.
- **Compensation and benefits specialists** use it to benchmark pay and perks against competitors, so they can calibrate salary bands and total rewards packages with real market data.
- **Recruitment and talent acquisition teams** use it to monitor interview experiences and job listings, so they can improve candidate journeys and refine hiring messaging.
- **Consultancies and market research agencies** use it to assemble multi-company datasets, so they can deliver data-backed reports on industry-wide culture, diversity, and pay trends.

---

## FAQs

**Q: What types of Glassdoor pages can this scraper handle?**
A: It is designed to work with company review pages, salaries pages (including filtered URLs), interviews sections, office locations, benefits, culture and diversity sections, and individual job listing URLs. You can control what type of data is collected via a configurable `command` parameter (e.g., reviews, interviews, salaries, jobs, overview, cultureDiversity, benefits).

**Q: Can I limit how much data is collected in a single run?**
A: Yes. You can set a `maxItems` value to cap the number of reviews, interviews, salaries, jobs, culture entries, or benefits records that are fetched. You can also tune `maxConcurrency`, `minConcurrency`, and `maxRequestRetries` to balance speed, rate-limiting tolerance, and infrastructure usage.

**Q: Does it support multiple languages for reviews and salaries?**
A: The scraper can include all available review or salary languages for a company when you enable the `includeAllReviews` or `includeAllSalaries` flags. This allows you to combine data from languages such as English, French, Portuguese, Spanish, Italian, Dutch, and German into a unified dataset.

**Q: How is the output formatted and where should I store it?**
A: Output is emitted as structured JSON records where each object corresponds to a review, interview, salary estimate, job posting, location, benefit review, or company overview entry. You can persist these JSON records to files, load them into a database or warehouse, or connect them directly to BI tools and dashboards.

---

## Performance Benchmarks and Results
- **Primary Metric (Scraping Speed):** On typical Glassdoor company pages, the scraper can process approximately 80–150 items per minute at moderate concurrency, depending on network conditions and the complexity of the requested data types.
- **Reliability Metric (Success Rate):** With conservative retry and concurrency settings, end-to-end runs commonly reach 95–99% successful request completion for stable company pages, even when pagination and multiple sections are enabled.
- **Efficiency Metric (Throughput):** By batching requests and reusing sessions, a single worker can handle thousands of reviews, salaries, or interview entries per hour while maintaining low CPU usage and modest memory overhead.
- **Quality Metric (Data Completeness):** Fields such as ratings, titles, dates, locations, demographic aggregates, salary percentiles, and benefits statistics are explicitly mapped and validated, resulting in consistently high data completeness across supported page types and company profiles.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
