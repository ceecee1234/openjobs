<p align="center">
  <img src="https://img.shields.io/badge/jobs-911+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-626+-purple?style=for-the-badge" alt="Companies">
  <img src="https://img.shields.io/badge/updated-every%206h-green?style=for-the-badge" alt="Update Frequency">
  <img src="https://img.shields.io/github/license/digidai/openjobs?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/digidai/openjobs?style=for-the-badge" alt="Stars">
</p>

<h1 align="center">OpenJobs</h1>

<p align="center">
  <strong>A free, open-source job aggregator that automatically collects and displays job listings from top companies.</strong>
</p>

<p align="center">
  <a href="https://digidai.github.io/openjobs">GitHub Pages</a> ·
  <a href="https://openjobs.genedai.me">Cloudflare Mirror</a> ·
  <a href="#features">Features</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#contributing">Contributing</a>
</p>

---

## Why OpenJobs?

Most job boards are cluttered with ads, require sign-ups, or hide the best listings behind paywalls. **OpenJobs** is different:

- **100% Free & Open Source** - No ads, no paywalls, no sign-ups
- **Auto-Updated Every 6 Hours** - Fresh jobs from 626+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 368 |
| Healthcare | 225 |
| Management | 112 |
| Engineering | 108 |
| Sales | 58 |
| Finance | 24 |
| Operations | 10 |
| Marketing | 4 |
| HR | 2 |

**Top Hiring Companies:** North Mississippi Health Services, Bloomberg, Eaton, Mosaic North America, MultiCare Health System

## Features

| Feature | Description |
|---------|-------------|
| **Auto Discovery** | Automatically finds and fetches the latest job data sources |
| **Smart Parsing** | Multi-format job caption parser (9+ strategies) for better data extraction |
| **Image Optimization** | CDN-powered image optimization with WebP conversion and lazy loading |
| **Smart Rotation** | Jobs rotate every 6 hours to show fresh content |
| **Dual Deployment** | GitHub Pages (table view) + Cloudflare Pages (card view) |
| **Company Logos** | Visual company branding for easy recognition |
| **Mobile Responsive** | Works perfectly on all device sizes |
| **SEO Enhanced** | Schema.org structured data, breadcrumbs, FAQ, and meta tags |
| **Accessibility** | WCAG compliant with ARIA labels, skip links, and keyboard navigation |
| **Daily Sitemaps** | SEO-friendly XML sitemaps updated automatically |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        GitHub Actions                           │
│                    (Scheduled every 6h)                         │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    update_readme.py                             │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────────────┐   │
│  │ Fetch XML   │ → │ Parse Jobs  │ → │ Generate Output     │   │
│  │ Sitemap     │   │ (911+ jobs) │   │ (README + HTML)     │   │
│  └─────────────┘   └─────────────┘   └─────────────────────┘   │
└─────────────────────────┬───────────────────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌─────────────────────┐       ┌─────────────────────┐
│   GitHub Pages      │       │  Cloudflare Pages   │
│   (README.md)       │       │  (public/index.html)│
│   Table Layout      │       │   Card Grid Layout  │
│   200 jobs/page     │       │   50 jobs/page      │
└─────────────────────┘       └─────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.11+
- Git

### Local Development

```bash
# Clone the repository
git clone https://github.com/digidai/openjobs.git
cd openjobs

# Run the update script
python scripts/update_readme.py

# View the generated files
open README.md           # GitHub Pages content
open public/index.html   # Cloudflare Pages content
```

### Deploy Your Own

1. **Fork this repository**

2. **Enable GitHub Pages**
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` / `root`

3. **Enable GitHub Actions**
   - Go to Actions tab
   - Enable workflows
   - Jobs will auto-update every 6 hours

4. **(Optional) Deploy to Cloudflare Pages**
   - Connect your forked repo
   - Build command: (none)
   - Output directory: `public`

## Configuration

Edit `scripts/update_readme.py` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| `JOBS_PER_PAGE` | 200 | Number of jobs shown on README |
| `HTML_JOBS_COUNT` | 50 | Number of jobs in HTML page |
| `ROTATION_HOURS` | 6 | Hours between job rotation |
| `CF_SITE_URL` | `https://openjobs.genedai.me` | Cloudflare Pages URL |
| `GH_SITE_URL` | `https://digidai.github.io/openjobs` | GitHub Pages URL |
| `IMAGE_CDN_ENABLED` | `True` | Enable/disable CDN image optimization |
| `IMAGE_CDN_URL` | `https://images.weserv.nl/?url=` | CDN service URL |
| `IMAGE_QUALITY` | 80 | Image quality (1-100) |
| `LOGO_WIDTH/HEIGHT` | 24 | Logo dimensions in pixels |

## Data Source

Jobs are aggregated from [OpenJobs AI](https://www.openjobs-ai.com), which collects listings from:

- **Tech**: Google, Amazon, Microsoft, Salesforce, SpaceX, and more
- **Healthcare**: Mayo Clinic, CVS Health, Northwell Health, and more
- **Finance**: CME Group, Fidelity, First Citizens Bank, and more
- **Retail**: Macy's, CVS, and more
- **And 626+ other companies**

## Project Structure

```
openjobs/
├── .github/
│   ├── workflows/          # GitHub Actions automation
│   └── ISSUE_TEMPLATE/     # Issue templates
├── scripts/
│   └── update_readme.py    # Main Python script
├── public/
│   ├── index.html          # Cloudflare Pages site
│   ├── stats.json          # Job statistics API
│   └── sitemap.xml         # Cloudflare sitemap
├── README.md               # This file (also GitHub Pages)
├── sitemap.xml             # GitHub Pages sitemap
├── _config.yml             # Jekyll configuration
├── LICENSE                 # MIT License
└── CONTRIBUTING.md         # Contribution guidelines
```

## Recent Enhancements

### 🚀 Performance & Quality Improvements (v2.0)

**Data Parsing (14.7x better location extraction)**
- Implemented 9-format job caption parser supporting:
  - `Title at Company in Location`
  - `Title at Company - Location`
  - `Title at Company | Location`
  - `Title - Company - Location`
  - `Title @ Company (Location)`
  - And more fallback strategies
- Location coverage improved from 0.4% to 6.28%

**Image Optimization**
- Free CDN integration (images.weserv.nl)
- Automatic WebP conversion with fallback
- Optimized dimensions (24x24px logos)
- Quality compression (80%)
- DNS prefetch and preconnection
- Lazy loading for better performance

**SEO Enhancements**
- Schema.org structured data:
  - BreadcrumbList for navigation
  - FAQPage for common questions
  - ItemList for job postings
  - Organization and WebSite schemas
- Enhanced meta tags (application-name, theme-color)
- Mobile web app capable

**Accessibility (WCAG Compliant)**
- Skip to main content link
- Comprehensive ARIA labels
- Keyboard navigation support
- Screen reader friendly
- Focus management

**Code Quality**
- Zero pyflakes warnings
- Enhanced error handling
- Detailed parse statistics
- Better logging and monitoring

## Roadmap

- [ ] Job search/filter functionality
- [ ] Job category tags
- [ ] Salary information (when available)
- [ ] Remote job filtering
- [ ] Email notifications for new jobs
- [ ] RSS feed support
- [x] Job statistics dashboard

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a PR.

### Ways to Contribute

- Report bugs or suggest features via [Issues](https://github.com/digidai/openjobs/issues)
- Improve documentation
- Add new features
- Optimize performance

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Job data provided by [OpenJobs AI](https://www.openjobs-ai.com)
- Hosted on [GitHub Pages](https://pages.github.com) and [Cloudflare Pages](https://pages.cloudflare.com)

---

<h2 align="center">Latest Job Openings</h2>

<p align="center">
  <em>Updated February 16, 2026 · Showing 200 of 911+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Firefighter/Paramedic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/8a/97f942ef9f787675ed38d2fe50182.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Akima | [View](https://www.openjobs-ai.com/jobs/firefighterparamedic-chattanooga-tn-135643107688448005) |
| 2026-2027 High School Special Education Science Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/68/5fdf44d53c902d34721e122bc450e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Coney Island Prep | [View](https://www.openjobs-ai.com/jobs/2026-2027-high-school-special-education-science-teacher-brooklyn-ny-135643107688448006) |
| Social Recreation Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/63/e29bb7737659bee3f6769800e5f25.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Boys and Girls Clubs of Boston | [View](https://www.openjobs-ai.com/jobs/social-recreation-assistant-boston-ma-135643107688448007) |
| Personal Injury Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/09/73076e4fd05346e7610cc1f50de4a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ascendion | [View](https://www.openjobs-ai.com/jobs/personal-injury-attorney-san-diego-ca-135643107688448008) |
| NP / PA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/5c/dc5bde0629db186a57cefe96e56f5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Surgery | [View](https://www.openjobs-ai.com/jobs/np-pa-surgery-trauma-columbia-columbia-sc-135643107688448009) |
| Corporate Planning & Management, Travel and Expense Management, Infrastructure, Associate, Dallas | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/60/bc2dc5944f9216badef737a3400d3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Goldman Sachs | [View](https://www.openjobs-ai.com/jobs/corporate-planning-management-travel-and-expense-management-infrastructure-associate-dallas-dallas-tx-135643107688448010) |
| Registered Nurse (RN) - Operating Room | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/91/59d977876480e94119a976fd1c393.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Catholic Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-operating-room-west-islip-ny-135643107688448011) |
| Associate Market General Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/4c/78cff44e309435774f26de659ec12.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ChenMed | [View](https://www.openjobs-ai.com/jobs/associate-market-general-manager-st-louis-mo-135643107688448012) |
| Registered Nurse (RN) - Medicine Oncology Unit | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/f6/4ad0a29a33a64fc7bfe57e8ad6601.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sentara Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-medicine-oncology-unit-virginia-beach-va-135643107688448013) |
| Nurse Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/48/6361208cc993991e2a9cf3f02442a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Surgical Services | [View](https://www.openjobs-ai.com/jobs/nurse-manager-surgical-services-richmond-community-richmond-va-135643107688448014) |
| Senior Desktop Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/32/56a66b6d7b126f270d536f49b0d7d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ropes & Gray LLP | [View](https://www.openjobs-ai.com/jobs/senior-desktop-engineer-washington-dc-135643107688448015) |
| Vice President, Treasury | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/d1/5030baa03875c241ef89f58d36faa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Affirm | [View](https://www.openjobs-ai.com/jobs/vice-president-treasury-austin-tx-135643107688448016) |
| Diesel Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/97/9e408e85a36377a9f1a17c6ab44fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Republic Services | [View](https://www.openjobs-ai.com/jobs/diesel-mechanic-lubbock-tx-135643107688448017) |
| Vice President, Treasury | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/d1/5030baa03875c241ef89f58d36faa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Affirm | [View](https://www.openjobs-ai.com/jobs/vice-president-treasury-sioux-falls-sd-135643107688448018) |
| Registered Nurse II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/16/eb7f343d8c9142856d7ab257ea40a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PRN | [View](https://www.openjobs-ai.com/jobs/registered-nurse-ii-prn-ed-camden-sc-135643107688448019) |
| Personal Injury Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/09/73076e4fd05346e7610cc1f50de4a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ascendion | [View](https://www.openjobs-ai.com/jobs/personal-injury-attorney-calabasas-ca-135643107688448020) |
| Insurance Coverage Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/09/73076e4fd05346e7610cc1f50de4a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ascendion | [View](https://www.openjobs-ai.com/jobs/insurance-coverage-attorney-chicago-il-135643107688448021) |
| Ambulatory Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/97/3fdfec10c6f726b11f273488ad009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Neurology Department | [View](https://www.openjobs-ai.com/jobs/ambulatory-nurse-neurology-department-headache-division-philadelphia-pa-135643107688448022) |
| Clinical Nurse 2-Med Surg (Cathcart 4- Cardio/ Tele)- PT-Days- Pennsylvania Hospital | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/97/3fdfec10c6f726b11f273488ad009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Penn Medicine, University of Pennsylvania Health System | [View](https://www.openjobs-ai.com/jobs/clinical-nurse-2-med-surg-cathcart-4-cardio-tele-pt-days-pennsylvania-hospital-philadelphia-pa-135643107688448023) |
| Registered Nurse II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/16/eb7f343d8c9142856d7ab257ea40a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CICU | [View](https://www.openjobs-ai.com/jobs/registered-nurse-ii-cicu-nights-columbia-sc-135643107688448024) |
| Advanced Practice Provider (NP/PA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/16/eb7f343d8c9142856d7ab257ea40a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Heart Failure ICU | [View](https://www.openjobs-ai.com/jobs/advanced-practice-provider-nppa-heart-failure-icu-columbia-sc-columbia-sc-135643107688448025) |
| ASSISTANT RESIDENTIAL MANAGER – CHILDREN'S RESIDENTIAL PROGRAM | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/ab/2c6549524e6069730393339af82c5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Developmental Disabilities Institute (DDI) | [View](https://www.openjobs-ai.com/jobs/assistant-residential-manager-childrens-residential-program-huntington-ny-135643107688448026) |
| Help Desk Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/0d/c30c8fcfe2f4e1cc4b02e4b882966.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pursuit Aerospace | [View](https://www.openjobs-ai.com/jobs/help-desk-analyst-cleveland-oh-135643107688448027) |
| Preschool Classroom Aide Substitute | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/a0/e8ff47963fb88f4bf9015d4a938c2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northeast Michigan Community Service Agency, Inc (NEMCSA) | [View](https://www.openjobs-ai.com/jobs/preschool-classroom-aide-substitute-caro-mi-135643107688448028) |
| Account Manager, Transport | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/bf/db79b53f8b754f47cf4a314195354.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hitachi Energy | [View](https://www.openjobs-ai.com/jobs/account-manager-transport-colorado-united-states-135643107688448029) |
| Staff Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/6c/c176b43e93e671584353d03957ff7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. Joseph's/Candler | [View](https://www.openjobs-ai.com/jobs/staff-nurse-savannah-ga-135643107688448030) |
| Regional Channel Sales Manager (Chicagoland) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/27/9ae599acc0f7f589e6b16ee93d5ce.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Avive Solutions Inc. | [View](https://www.openjobs-ai.com/jobs/regional-channel-sales-manager-chicagoland-chicago-il-135643107688448031) |
| Family Educator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/a0/e8ff47963fb88f4bf9015d4a938c2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northeast Michigan Community Service Agency, Inc (NEMCSA) | [View](https://www.openjobs-ai.com/jobs/family-educator-gaylord-mi-135643107688448032) |
| ATI CAS LOADMASTER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/66/896394c4a3c1865c39b8716eabefe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Air Transport International, Inc. | [View](https://www.openjobs-ai.com/jobs/ati-cas-loadmaster-united-states-135643107688448033) |
| Speech Language Pathologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/54/4edcfdaace206b9adc30afa785e24.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MGA Homecare | [View](https://www.openjobs-ai.com/jobs/speech-language-pathologist-denver-co-135643107688448034) |
| Retail Sales Representative - Lighting Design Center | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/c2/93623be5d67abd5a485681516360a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bayside Electric Supply Company Inc | [View](https://www.openjobs-ai.com/jobs/retail-sales-representative-lighting-design-center-wilmington-nc-135643107688448035) |
| System Design Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/93/d39a3628c89286802f7fd73461a44.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> xAI | [View](https://www.openjobs-ai.com/jobs/system-design-specialist-palo-alto-ca-135643107688448036) |
| Medical Assistant - Concierge | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/26/351332e42132d928cab3837419167.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jupiter Medical Center | [View](https://www.openjobs-ai.com/jobs/medical-assistant-concierge-jupiter-fl-135643107688448037) |
| Field Service Engineer - Western | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/60/7c4e8cca3a8fffacac70ce32b70ec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LECO | [View](https://www.openjobs-ai.com/jobs/field-service-engineer-western-united-states-135643107688448038) |
| Warehouse Material Handler Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/a2/44ba77adbb29a40182f24da55f5b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> U.S. AutoForce | [View](https://www.openjobs-ai.com/jobs/warehouse-material-handler-lead-minneapolis-mn-135643107688448040) |
| FT/PT LPN/RN Homecare | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/54/4edcfdaace206b9adc30afa785e24.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MGA Homecare | [View](https://www.openjobs-ai.com/jobs/ftpt-lpnrn-homecare-winston-salem-nc-135643107688448041) |
| Aircraft Maintenance Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/ef/9d2d01d31514a6e0798f7474fa97e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ACI Jet | [View](https://www.openjobs-ai.com/jobs/aircraft-maintenance-technician-san-luis-obispo-ca-135643107688448042) |
| Internal Auditor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/e0/d5608a466a7bcb195083b6c2649ed.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Toyota Tsusho America | [View](https://www.openjobs-ai.com/jobs/internal-auditor-georgetown-ky-135643107688448043) |
| Patient Care Tech Full Time Days | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/cf/cdbfd20f03eb342877ff91b76567e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> United Surgical Partners International, Inc | [View](https://www.openjobs-ai.com/jobs/patient-care-tech-full-time-days-oklahoma-city-ok-135643355152384000) |
| Certified Nursing Assistant (CNA) - Full Time, Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/1e/8cdfd7969c10c48477fca34ec8861.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Williamsburg Landing | [View](https://www.openjobs-ai.com/jobs/certified-nursing-assistant-cna-full-time-part-time-williamsburg-va-135643355152384001) |
| Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1d/1faebca23841b08454d777591bf9f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Actalent | [View](https://www.openjobs-ai.com/jobs/planner-meriden-ct-135643355152384002) |
| Supply Technicians | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/07/b3f869f05046daa1c9c95e4c308f3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vanguard Companies | [View](https://www.openjobs-ai.com/jobs/supply-technicians-newport-nc-135643355152384003) |
| Civil Engineer - Land Development | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/a9/310050a19998d740861909792e685.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MCBRIDE HOMES LIMITED | [View](https://www.openjobs-ai.com/jobs/civil-engineer-land-development-chesterfield-mo-135643355152384004) |
| Histotechnician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/c7/08699ea56439fdfbfffbc4d78180c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Labcorp | [View](https://www.openjobs-ai.com/jobs/histotechnician-houston-tx-135643355152384005) |
| Customer Service &amp; Onboarding Specialist (Temporary, Part-Time) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/customer-service-amp-onboarding-specialist-temporary-part-time-lowell-ma-135643355152384006) |
| Research Professional - Johnson Maynard Lab | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/research-professional-johnson-maynard-lab-athens-ga-135643355152384007) |
| Physician-Scientist or Scientist Faculty Scholars, Center for Pediatric IBD and Celiac Disease | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/physician-scientist-or-scientist-faculty-scholars-center-for-pediatric-ibd-and-celiac-disease-stanford-ca-135643355152384008) |
| Senior Business Development and Licensing Manager- Life Sciences and Digital Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/senior-business-development-and-licensing-manager-life-sciences-and-digital-health-hanover-nh-135643355152384009) |
| Customer Service Immediate Hire | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/79/f31a67a67d7f322aa7b3807b0c788.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aston Carter | [View](https://www.openjobs-ai.com/jobs/customer-service-immediate-hire-framingham-ma-135643355152384011) |
| Marine Painter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1d/1faebca23841b08454d777591bf9f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Actalent | [View](https://www.openjobs-ai.com/jobs/marine-painter-norfolk-va-135643355152384012) |
| Manager, Government Finance (Onsite) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/67/46319c6eccacac60477517db0c1e9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pratt & Whitney | [View](https://www.openjobs-ai.com/jobs/manager-government-finance-onsite-east-hartford-ct-135643355152384013) |
| Community School Site Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2a/c9121eed1184400231b9925700c89.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Center for Youth Services, Inc. | [View](https://www.openjobs-ai.com/jobs/community-school-site-coordinator-irondequoit-ny-135643355152384014) |
| Project Manager, Integrated Water Management Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/d9/5ed8c1e93b47def4e766bdb9cb4ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stantec | [View](https://www.openjobs-ai.com/jobs/project-manager-integrated-water-management-specialist-walnut-creek-ca-135643355152384015) |
| Airport Accessibility College Intern- Culture & Strategy: Airport Access & Business Opportunity - Denver International Airport | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/15/f71c2dcdfb534921bba42865da88a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City and County of Denver | [View](https://www.openjobs-ai.com/jobs/airport-accessibility-college-intern-culture-strategy-airport-access-business-opportunity-denver-international-airport-denver-co-135643355152384016) |
| Business Development Center Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/f0/c007a9faddc5e71a18b38d4237a80.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Phil Long Dealerships | [View](https://www.openjobs-ai.com/jobs/business-development-center-representative-colorado-springs-co-135643355152384017) |
| Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/42/b49b72ea8b3f2fd32b9fa1595c53f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Premier Therapy LLC | [View](https://www.openjobs-ai.com/jobs/physical-therapist-groton-ny-135643355152384018) |
| SPEECH THERAPIST | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/0c/a86f378f472b1829c263698cd59cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Live Well Homecare | [View](https://www.openjobs-ai.com/jobs/speech-therapist-hallettsville-tx-135643355152384020) |
| Refrigeration Technician (St. Louis) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/c7/73c60c19c76e93a9b39a1c1f58dc7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Innovative Refrigeration Systems, Inc. | [View](https://www.openjobs-ai.com/jobs/refrigeration-technician-st-louis-st-louis-mo-135643355152384021) |
| Dean of the College of Environment and Design | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/dean-of-the-college-of-environment-and-design-athens-ga-135643355152384022) |
| Adjunct Assistant Professor, Developmental Education (English) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/adjunct-assistant-professor-developmental-education-english-gainesville-fl-135643355152384023) |
| Sociology of Circular Bioeconomy Systems - Research Assistant/Associate/Full Professor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/sociology-of-circular-bioeconomy-systems-research-assistantassociatefull-professor-knoxville-tn-135643355152384024) |
| Government & Regulatory Affairs, Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/3b/a853a78e93a27dcc0a0ff21c61465.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aypa Power | [View](https://www.openjobs-ai.com/jobs/government-regulatory-affairs-intern-austin-tx-135643355152384025) |
| Data Management Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/data-management-tutor-round-rock-tx-135643556478976000) |
| CAPM Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/capm-tutor-roswell-ga-135643556478976001) |
| Law Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/law-tutor-johns-creek-ga-135643556478976002) |
| Lua Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/lua-tutor-oak-lawn-il-135643556478976003) |
| AP Physics Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/ap-physics-tutor-fort-lauderdale-fl-135643556478976004) |
| AP Physics C: Mechanics Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/ap-physics-c-mechanics-tutor-jacksonville-fl-135643556478976005) |
| ARDMS | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RDCS | [View](https://www.openjobs-ai.com/jobs/ardms-rdcs-pediatric-echocardiography-pe-tutor-bridgeport-ct-135643556478976006) |
| Electromagnetism Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/electromagnetism-tutor-wichita-ks-135643556478976007) |
| GRE Subject Test in Mathematics Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/gre-subject-test-in-mathematics-tutor-memphis-tn-135643556478976008) |
| Strategic Sourcing Manager - Marketing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/9a/23cbc455158951716b440c3d165e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Meta | [View](https://www.openjobs-ai.com/jobs/strategic-sourcing-manager-marketing-menlo-park-ca-135641404801024320) |
| Senior Software Engineer - Dynamics 365 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/01/b3620c3be49fbf4948033d9de9814.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EPAM Systems | [View](https://www.openjobs-ai.com/jobs/senior-software-engineer-dynamics-365-weehawken-nj-135641404801024321) |
| AVP, Product Development Attorney - Professional Liability | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/39/fc6fb50c435b5f4f06584523b2325.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arch Insurance Group Inc. | [View](https://www.openjobs-ai.com/jobs/avp-product-development-attorney-professional-liability-hartford-ct-135641404801024322) |
| Young Adult Peer Mentor (Youth Quake) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/66/03acc5b66c559178b295953a0bdd2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vinfen | [View](https://www.openjobs-ai.com/jobs/young-adult-peer-mentor-youth-quake-lowell-ma-135641404801024323) |
| Production Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/27/d33835a1a293675d10683c9481c95.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Austin Allen Company | [View](https://www.openjobs-ai.com/jobs/production-manager-claremore-ok-135641404801024325) |
| Physician, Integrative Medicine (Santa Rosa, CA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/b4/201dff67a95846941fe2550d31cd8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter West Bay Medical Group | [View](https://www.openjobs-ai.com/jobs/physician-integrative-medicine-santa-rosa-ca-santa-rosa-ca-135641404801024326) |
| Staff Analog AI Compute Architect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/10/19c7a2fa7caa73285924e0b39d04d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Analog Devices | [View](https://www.openjobs-ai.com/jobs/staff-analog-ai-compute-architect-boston-ma-135641404801024327) |
| Vice President, Product Development – CMC, Gene Therapy and Large Molecules | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/8e/09352826ddcffddd04f2b791a410a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insmed Incorporated | [View](https://www.openjobs-ai.com/jobs/vice-president-product-development-cmc-gene-therapy-and-large-molecules-headquarters-nj-135641404801024328) |
| Product Demonstrator Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/5d/7affe96fe46d9e9d7d04b434f7be5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Product Connections | [View](https://www.openjobs-ai.com/jobs/product-demonstrator-part-time-hendersonville-nc-135641404801024329) |
| Production Technician - Combustion Spray Pyrolysis | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/03/3c37e1e944c1967bdf16bae4b808c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Linde Advanced Material Technologies | [View](https://www.openjobs-ai.com/jobs/production-technician-combustion-spray-pyrolysis-indianapolis-in-135641404801024330) |
| Senior Tax Associate/Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/c3/c084e7625114efc3386fa4f387581.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Friedman + Huey Associates LLP | [View](https://www.openjobs-ai.com/jobs/senior-tax-associatesupervisor-greater-chicago-area-135641404801024331) |
| Welder - 2nd Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/61/1c2a45dc85d66a651f743f9e49e46.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rittal LLC | [View](https://www.openjobs-ai.com/jobs/welder-2nd-shift-urbana-oh-135641404801024332) |
| Automotive Operations Support Manager (Remote MI & IN) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/c5/1361c2560f2de17e3a6e5f2154fe6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dent Wizard International | [View](https://www.openjobs-ai.com/jobs/automotive-operations-support-manager-remote-mi-in-indiana-united-states-135641404801024333) |
| Production Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/cf/4441791f915d9d8f28fb3b08acae0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Avient Corporation | [View](https://www.openjobs-ai.com/jobs/production-associate-north-haven-ct-135641404801024334) |
| Sr. Product Development Engineer, Biomaterials | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/80/428d5eae7943c0ce3c4301444b229.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Secant Group | [View](https://www.openjobs-ai.com/jobs/sr-product-development-engineer-biomaterials-telford-pa-135641404801024335) |
| PET/CT Technologist; 1 day a week! $60.00/hour | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/76/601b1d9f88a6a5c3e22825724418e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DMS Health Technologies | [View](https://www.openjobs-ai.com/jobs/petct-technologist-1-day-a-week-6000hour-seaford-de-135641404801024336) |
| Surgical Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/cf/9fb364b2be4e45830b16715f5a74a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. Joseph's Health | [View](https://www.openjobs-ai.com/jobs/surgical-technologist-paterson-nj-135641404801024337) |
| Bus Mechanic (A) Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/d7/86b122fe87ee68addcf1ba2b79e17.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 320 | [View](https://www.openjobs-ai.com/jobs/bus-mechanic-a-lead-320-transit-vehicle-maintenance-2nd-shift-wichita-ks-135641404801024338) |
| Certified Surg Tech-First Assist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/4c/8bcc5e0715400e98890ef06dc45ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WVU Medicine Princeton Community Hospital | [View](https://www.openjobs-ai.com/jobs/certified-surg-tech-first-assist-princeton-wv-135641404801024339) |
| Driver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/9d/79f0b46929b9fdcd3b849621cf917.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sevita | [View](https://www.openjobs-ai.com/jobs/driver-canton-oh-135641404801024340) |
| Google Holiday Sales Associate Program 2025 – Be the Spark Behind the Season! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/23/5bb06f5d961ec4349a957ab2ca6f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mosaic North America | [View](https://www.openjobs-ai.com/jobs/google-holiday-sales-associate-program-2025-be-the-spark-behind-the-season-west-hollywood-ca-135641404801024341) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fb/881bf3e57eb8b3449a49aacbd9a48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MultiCare Health System | [View](https://www.openjobs-ai.com/jobs/registered-nurse-tacoma-wa-135641404801024342) |
| Finance Manager, Business Technology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/d7/03855811eccad9729b3a621e165bb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Okta | [View](https://www.openjobs-ai.com/jobs/finance-manager-business-technology-san-francisco-ca-135641404801024343) |
| Business Development Mgr (Unmanned Surface Vessels) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/41/b5e9052ff5ec6b932abea116afa16.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Textron | [View](https://www.openjobs-ai.com/jobs/business-development-mgr-unmanned-surface-vessels-hunt-valley-md-135641404801024344) |
| Account Manager - New York, NY | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/00/4a236508797a923348109a8964573.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Blackbird Labs | [View](https://www.openjobs-ai.com/jobs/account-manager-new-york-ny-new-york-united-states-135641404801024345) |
| Welder | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/fc/8932b375b142108349f1af703acd6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ludlow Mfg Inc | [View](https://www.openjobs-ai.com/jobs/welder-waukegan-il-135641404801024346) |
| Express Tech - Phil Hughes Honda | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/b5/24bc56f75ec605d85765f45ba57d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Phil Hughes Automotive Group | [View](https://www.openjobs-ai.com/jobs/express-tech-phil-hughes-honda-athens-ga-135641404801024347) |
| Direct Support Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/9d/79f0b46929b9fdcd3b849621cf917.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sevita | [View](https://www.openjobs-ai.com/jobs/direct-support-professional-clinton-ia-135641404801024348) |
| Case Manager - Pediatric Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fb/881bf3e57eb8b3449a49aacbd9a48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MultiCare Health System | [View](https://www.openjobs-ai.com/jobs/case-manager-pediatric-home-health-tacoma-wa-135641404801024349) |
| Staff Product Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/c9/6880deefc8e5eeb395dbb19944c64.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Polymarket | [View](https://www.openjobs-ai.com/jobs/staff-product-designer-new-york-united-states-135641404801024350) |
| CRITICAL CARE TECHNICIAN - MODIFIED CARE UNIT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/a8/801a66d90cf3c432cd6cb347a6c6b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Froedtert Health | [View](https://www.openjobs-ai.com/jobs/critical-care-technician-modified-care-unit-west-bend-wi-135641404801024352) |
| CJ3 Captain | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/9d/9e2eabfe665329850c9ceefbb4104.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> FlyUSA | [View](https://www.openjobs-ai.com/jobs/cj3-captain-tampa-fl-135641404801024353) |
| Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/a6/146e1567a91edae75d50470ca4ef5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Physical Therapy & Sports Medicine Centers | [View](https://www.openjobs-ai.com/jobs/physical-therapist-new-london-county-ct-135641404801024354) |
| Aerospace Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/bc/df2a94a8ad3e0f6831ca2e42e582b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Autocam Medical | [View](https://www.openjobs-ai.com/jobs/aerospace-engineer-murfreesboro-tn-135641404801024355) |
| Maintenance Supervisor -Mechanical, Electrical, Plumbing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/a1/290af73f272b6a2c3a074e7986964.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cabell Huntington Hospital | [View](https://www.openjobs-ai.com/jobs/maintenance-supervisor-mechanical-electrical-plumbing-huntington-wv-135641404801024356) |
| Product Manager - Investment Accounting Analytics | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f1/70932743e65054b272ce3780bb908.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bloomberg | [View](https://www.openjobs-ai.com/jobs/product-manager-investment-accounting-analytics-new-york-ny-135641404801024357) |
| Senior Software Engineer - Kubernetes as a Service | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f1/70932743e65054b272ce3780bb908.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bloomberg | [View](https://www.openjobs-ai.com/jobs/senior-software-engineer-kubernetes-as-a-service-new-york-ny-135641404801024358) |
| Division Vice President, AI Safety | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/44/84c79ef0b9d2fa08fc7a385791df1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TaskUs | [View](https://www.openjobs-ai.com/jobs/division-vice-president-ai-safety-austin-tx-135641404801024359) |
| RN Field Supervisor (Bilingual Spanish/Manhattan) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/19/057f852c9491a0a1a0e8196a7fd42.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> VNS Health | [View](https://www.openjobs-ai.com/jobs/rn-field-supervisor-bilingual-spanishmanhattan-new-york-ny-135641404801024360) |
| Medical Lab Scientist (MLS) - St. Charles Hospital | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/46/79e609f5af0ee23f41c2c44408754.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bon Secours Mercy Health | [View](https://www.openjobs-ai.com/jobs/medical-lab-scientist-mls-st-charles-hospital-oregon-oh-135641404801024361) |
| Regional Accounting Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/9e/38475db0aff5edeb9380027b0cfa6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Covenant Living Communities and Services | [View](https://www.openjobs-ai.com/jobs/regional-accounting-analyst-skokie-il-135641404801024362) |
| Technical Sourcer, Engineering (Temporary) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/eb/133e4dead5f8e42c83c35eaf535cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Render | [View](https://www.openjobs-ai.com/jobs/technical-sourcer-engineering-temporary-united-states-135641404801024363) |
| Case Manager (Personal Injury) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/a9/0b96dbdcb1d91e7a4991b9265cd4e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Capital Law Firm, P.C. | [View](https://www.openjobs-ai.com/jobs/case-manager-personal-injury-los-angeles-ca-135641404801024364) |
| Image Architect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/9a/23cbc455158951716b440c3d165e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Meta | [View](https://www.openjobs-ai.com/jobs/image-architect-sunnyvale-ca-135641404801024365) |
| Continuous Improvement Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/77/c815d747327d43c9d29e7693a8b1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vivint | [View](https://www.openjobs-ai.com/jobs/continuous-improvement-analyst-lehi-ut-135641404801024366) |
| Registered Nurse, Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/be/e2db445ab9caf54973d2c3d730de2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CenterWell Home Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-home-health-beaumont-tx-135641404801024367) |
| Aux Security Personnel PRN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/48/74f0949b7736752da518b078f098b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vanderbilt University Medical Center | [View](https://www.openjobs-ai.com/jobs/aux-security-personnel-prn-lebanon-tn-135641404801024368) |
| Steward/Stewardess Captain | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/bb/0772f0e6d00ade574ba52b0eb55af.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Food & Nutrition Services | [View](https://www.openjobs-ai.com/jobs/stewardstewardess-captain-food-nutrition-services-part-time-70-los-angeles-ca-135641404801024369) |
| Data & Analytics Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/8a/2e1927fdb063d482728bc0a885a89.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> rockITdata | [View](https://www.openjobs-ai.com/jobs/data-analytics-consultant-united-states-135641404801024370) |
| 2026 Summer Internship Program: Global Manufacturing Science (GMSci) Small Molecule API Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4b/a4b80b3c7c8a74242014202aa3ced.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Takeda | [View](https://www.openjobs-ai.com/jobs/2026-summer-internship-program-global-manufacturing-science-gmsci-small-molecule-api-intern-boston-ma-135641404801024371) |
| Neurophysiologist (New York, NY) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ea/ff5ae9a836c08bb57beaa701dc658.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Globus Medical | [View](https://www.openjobs-ai.com/jobs/neurophysiologist-new-york-ny-new-york-united-states-135641404801024372) |
| Manager, Tax - Large Corp | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/f3/1cf07abd9362861f6b9fe9f1818c4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Forvis Mazars US | [View](https://www.openjobs-ai.com/jobs/manager-tax-large-corp-tysons-corner-va-135641404801024373) |
| RF Systems Engineer - Mission Payloads | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/15/2bbfa9be15134984ddfc16749aa04.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> York Space Systems | [View](https://www.openjobs-ai.com/jobs/rf-systems-engineer-mission-payloads-greenwood-village-co-135641404801024374) |
| Sales Manager - Alliedstar | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7a/d14752ad02ada63031185978b9e0d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Straumann Group | [View](https://www.openjobs-ai.com/jobs/sales-manager-alliedstar-denver-co-135641404801024375) |
| Physical Therapist – Hand & Upper Extremity Focus | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/41/df1043497435ef5b84415d7595f5b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HAND THERAPY OF WYOMING LLC | [View](https://www.openjobs-ai.com/jobs/physical-therapist-hand-upper-extremity-focus-buffalo-wy-135641404801024376) |
| Hiring Cardiovascular Surgeon for Academic Health System in Reno/Tahoe | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/b9/e902226bbe7a2b265ef3dc88366de.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Renown Health | [View](https://www.openjobs-ai.com/jobs/hiring-cardiovascular-surgeon-for-academic-health-system-in-renotahoe-reno-nv-135641404801024377) |
| Sr Product Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/0a/058baaeef16e88f6bd2ee36c03f6f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PayPal | [View](https://www.openjobs-ai.com/jobs/sr-product-manager-san-jose-ca-135641404801024378) |
| Senior Software Engineer - Fixed Income and Derivatives | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f1/70932743e65054b272ce3780bb908.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bloomberg | [View](https://www.openjobs-ai.com/jobs/senior-software-engineer-fixed-income-and-derivatives-new-york-ny-135641404801024379) |
| ACCS Residential Counselor (24 Hours) - School Street | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/eb/6e733a4f82c8d89b85d3ac62a50b6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Bridge of Central Massachusetts | [View](https://www.openjobs-ai.com/jobs/accs-residential-counselor-24-hours-school-street-fitchburg-ma-135641404801024380) |
| Physical Therapist - Outpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/06/f77f8841a3f9b8f6e42bcc622d992.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PT Solutions Physical Therapy | [View](https://www.openjobs-ai.com/jobs/physical-therapist-outpatient-stockbridge-ga-135641404801024382) |
| Physical Therapist, Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/be/e2db445ab9caf54973d2c3d730de2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CenterWell Home Health | [View](https://www.openjobs-ai.com/jobs/physical-therapist-home-health-albany-tx-135641404801024383) |
| Google Holiday Sales Associate Program 2025 – Be the Spark Behind the Season! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/23/5bb06f5d961ec4349a957ab2ca6f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mosaic North America | [View](https://www.openjobs-ai.com/jobs/google-holiday-sales-associate-program-2025-be-the-spark-behind-the-season-beaverton-or-135641404801024384) |
| Lab Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/f8/8933718c6c7496e8683971c4c437e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AmSpec Group | [View](https://www.openjobs-ai.com/jobs/lab-coordinator-texas-city-tx-135641404801024385) |
| KBI: US - Manufacturing Associate I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/ec/e33ab377f83ba76f55bd45cdf145a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> KBI Biopharma | [View](https://www.openjobs-ai.com/jobs/kbi-us-manufacturing-associate-i-durham-nc-135641404801024386) |
| Physical Therapist-Up to 10K Sign on Bonus-OnSite | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/1d/58886723690e9e5890c26b2ced8a8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Foothills Sports Medicine Physical Therapy | [View](https://www.openjobs-ai.com/jobs/physical-therapist-up-to-10k-sign-on-bonus-onsite-peoria-az-135641404801024387) |
| Enterprise Data Architect (Hybrid OR Remote- Jersey City, Raleigh, or Hartford) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/48/ff3f38303f998a326b8b925f79adc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arch Capital Group Ltd. | [View](https://www.openjobs-ai.com/jobs/enterprise-data-architect-hybrid-or-remote-jersey-city-raleigh-or-hartford-district-of-columbia-united-states-135641404801024388) |
| Sales Manager - Alliedstar | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7a/d14752ad02ada63031185978b9e0d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Straumann Group | [View](https://www.openjobs-ai.com/jobs/sales-manager-alliedstar-jacksonville-fl-135641404801024389) |
| Spanish Speaking PTA Physical Therapy Assistant  for Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/07/a7ff62db49bf5946e6405f08650c3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> FeldCare Connects | [View](https://www.openjobs-ai.com/jobs/spanish-speaking-pta-physical-therapy-assistant-for-home-health-diamond-bar-ca-135641404801024390) |
| Primary Care Physician - Dublin (Perimeter) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/fc/940a81e8f0dec4507ca4a59a5549d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ohio State University Physicians | [View](https://www.openjobs-ai.com/jobs/primary-care-physician-dublin-perimeter-dublin-oh-135641404801024391) |
| Bilingual Front Desk Receptionist (Torrance) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/23/1c5edc480ffb7c9817b486db24b9c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wilshire Law Firm | [View](https://www.openjobs-ai.com/jobs/bilingual-front-desk-receptionist-torrance-torrance-ca-135641404801024393) |
| Patient Care Assistant Attendant- Aging Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/8c/eeac0def2b30c55c283969729c036.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UnityPoint Health | [View](https://www.openjobs-ai.com/jobs/patient-care-assistant-attendant-aging-services-cedar-rapids-ia-135641404801024394) |
| Medical Malpractice Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/f7/1dd18d21a3bfa2f43c00266596d60.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Morgan & Morgan, P.A. | [View](https://www.openjobs-ai.com/jobs/medical-malpractice-attorney-charleston-sc-135641404801024395) |
| Tax Principal - Banking and Specialty Finance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/d0/aa75c241dba6e00699f9ff7a3dce5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CLA (CliftonLarsonAllen) | [View](https://www.openjobs-ai.com/jobs/tax-principal-banking-and-specialty-finance-des-moines-ia-135641404801024396) |
| Licensed Clinical Social Worker - LCSW | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/ed/7a4545db8b9b6b6a64a0fe70059ed.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> McHur Care | [View](https://www.openjobs-ai.com/jobs/licensed-clinical-social-worker-lcsw-lubbock-tx-135641404801024397) |
| System Director Nursing Operations & Workforce Integration | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/4f/ea93079e0a8e0f39e6da66e8ad4fb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AMN Healthcare Leadership Solutions | [View](https://www.openjobs-ai.com/jobs/system-director-nursing-operations-workforce-integration-wausau-wi-135641404801024398) |
| CNC Machinist - 1st Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/c6/f8dc38cc16d6bfbc07d8f8ace3e41.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trace-A-Matic | [View](https://www.openjobs-ai.com/jobs/cnc-machinist-1st-shift-brookfield-wi-135641404801024399) |
| Care Coordinator, RN Field Based | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/d7/2026e678572fd289e8002534c94c9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Humana | [View](https://www.openjobs-ai.com/jobs/care-coordinator-rn-field-based-indiana-united-states-135641404801024400) |
| Journeyman Electrician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/66/8690a405f9440c8b0c8bbdc9dcbfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lane Valente Industries | [View](https://www.openjobs-ai.com/jobs/journeyman-electrician-greensburg-pa-135641404801024401) |
| Clinical Pharmacist (PRN \| As Needed) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/c3/f0c650e75bbba38ddf5c2a65c6d4e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Children's National Hospital | [View](https://www.openjobs-ai.com/jobs/clinical-pharmacist-prn-as-needed-washington-dc-baltimore-area-135641404801024402) |
| Facilities Engineering Design Associate Architect II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/8e/22f0278a5d9bd8bd71b72b45d9e53.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Blue Origin | [View](https://www.openjobs-ai.com/jobs/facilities-engineering-design-associate-architect-ii-huntsville-al-135641404801024403) |
| Technical Program Manager  - Design for Manufacturability (DFM, PCBA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/5f/bbb255ec03eb61f6498d45b544a75.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tata Electronics | [View](https://www.openjobs-ai.com/jobs/technical-program-manager-design-for-manufacturability-dfm-pcba-santa-clara-ca-135641404801024404) |
| Regional Sales Director, Mid-Atlantic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/9e/a5c14b5acf08e16f3f63146054921.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Invivyd | [View](https://www.openjobs-ai.com/jobs/regional-sales-director-mid-atlantic-washington-pa-135641404801024405) |
| Tech, Forensic Toxicology Laboratory Processing I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/b6/024ac3e2a930ca3de64b939488e62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Quest Diagnostics | [View](https://www.openjobs-ai.com/jobs/tech-forensic-toxicology-laboratory-processing-i-lenexa-ks-135641404801024406) |
| Juice Barista Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/5d/7affe96fe46d9e9d7d04b434f7be5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Product Connections | [View](https://www.openjobs-ai.com/jobs/juice-barista-part-time-raymore-mo-135641404801024407) |
| Customer Service Representative - Frisco | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/9e/e25d3c55fcf427c2cf36008236f51.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alpine Bank | [View](https://www.openjobs-ai.com/jobs/customer-service-representative-frisco-frisco-co-135641404801024408) |
| Speech Therapist, Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/be/e2db445ab9caf54973d2c3d730de2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CenterWell Home Health | [View](https://www.openjobs-ai.com/jobs/speech-therapist-home-health-seattle-wa-135641404801024409) |
| CEMA Senior SEIT Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/8d/e76be154592094de23849bed78daa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BAE Systems, Inc. | [View](https://www.openjobs-ai.com/jobs/cema-senior-seit-lead-hudson-nh-135641404801024410) |
| REG NURSE-SPARROW HOME HOSPICE | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/3d/5ff2c7d445a8c0b5de14683944ded.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> University of Michigan Health-Sparrow | [View](https://www.openjobs-ai.com/jobs/reg-nurse-sparrow-home-hospice-lansing-mi-135641404801024411) |
| Google Holiday Sales Associate Program 2025 – Be the Spark Behind the Season! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/23/5bb06f5d961ec4349a957ab2ca6f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mosaic North America | [View](https://www.openjobs-ai.com/jobs/google-holiday-sales-associate-program-2025-be-the-spark-behind-the-season-salt-lake-city-ut-135641404801024412) |
| Engineering Technician II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/19/4aad4cdad072d07bedc2198ea771d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sigma Design | [View](https://www.openjobs-ai.com/jobs/engineering-technician-ii-redmond-wa-135641404801024413) |
| SAP EWM Functional Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/29/9dedca4f518f26fa16795d17d9aa9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cognitus | [View](https://www.openjobs-ai.com/jobs/sap-ewm-functional-consultant-united-states-135641404801024414) |
| RN Critical Care MICU | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/46/79e609f5af0ee23f41c2c44408754.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bon Secours Mercy Health | [View](https://www.openjobs-ai.com/jobs/rn-critical-care-micu-youngstown-oh-135641404801024415) |
| Physical Therapist - Outpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/06/f77f8841a3f9b8f6e42bcc622d992.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PT Solutions Physical Therapy | [View](https://www.openjobs-ai.com/jobs/physical-therapist-outpatient-shelby-nc-135641404801024416) |
| Retail Store Team Leader (Part-Time) - Schaumburg, IL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/11/f4889f0b43c1a20685b9c87251878.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> the LEGO Group | [View](https://www.openjobs-ai.com/jobs/retail-store-team-leader-part-time-schaumburg-il-schaumburg-il-135641404801024417) |
| Registered Nurse- Surgical Oncology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/1f/82e49bae801110e99bcd57841853d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Indiana University Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-surgical-oncology-indianapolis-in-135641404801024418) |
| Sales Manager - Alliedstar | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7a/d14752ad02ada63031185978b9e0d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Straumann Group | [View](https://www.openjobs-ai.com/jobs/sales-manager-alliedstar-lincoln-ne-135641404801024419) |
| Per Diem Registered Nurse - Float Pool | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/cf/9fb364b2be4e45830b16715f5a74a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. Joseph's Health | [View](https://www.openjobs-ai.com/jobs/per-diem-registered-nurse-float-pool-wayne-nj-135641404801024420) |
| Product Demonstrator Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/5d/7affe96fe46d9e9d7d04b434f7be5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Product Connections | [View](https://www.openjobs-ai.com/jobs/product-demonstrator-part-time-pittsburgh-pa-135641404801024421) |
| Team Leader - Pharmacovigilance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/79/c0cb0ed2dc25db121283f7a98cc71.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Elanco | [View](https://www.openjobs-ai.com/jobs/team-leader-pharmacovigilance-lake-county-in-135641404801024422) |
| Registered Nurse, Emergency Department, Full Time, Night | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/ed/79abef0899104f5b6003e08e57d72.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Valley Health System | [View](https://www.openjobs-ai.com/jobs/registered-nurse-emergency-department-full-time-night-paramus-nj-135641404801024423) |
| Portfolio Manager Senior | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/f1/d4e01801a0877ea2d864b32c1a98d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> United Community | [View](https://www.openjobs-ai.com/jobs/portfolio-manager-senior-knoxville-tn-135641404801024424) |
| CNA/HHA - Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/91/ba3790fe06726cf8da9cd9969db32.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Benchmark Senior Living | [View](https://www.openjobs-ai.com/jobs/cnahha-part-time-quincy-ma-135641404801024425) |
| I.P. - Technology Transactions (Life Sciences) Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/32/7688204ad83e84ade64902c8606c8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fenwick & West | [View](https://www.openjobs-ai.com/jobs/ip-technology-transactions-life-sciences-associate-boston-ma-135641404801024426) |
| Product and Licensing Counsel | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f1/70932743e65054b272ce3780bb908.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bloomberg | [View](https://www.openjobs-ai.com/jobs/product-and-licensing-counsel-new-york-ny-135641404801024427) |
| Certified Medical Assistant Musculoskeletal Neuro | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fb/881bf3e57eb8b3449a49aacbd9a48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MultiCare Health System | [View](https://www.openjobs-ai.com/jobs/certified-medical-assistant-musculoskeletal-neuro-spokane-valley-wa-135641404801024428) |
| Tax Manager/Director - Banking and Specialty Finance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/d0/aa75c241dba6e00699f9ff7a3dce5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CLA (CliftonLarsonAllen) | [View](https://www.openjobs-ai.com/jobs/tax-managerdirector-banking-and-specialty-finance-st-cloud-mn-135641404801024429) |
| Global Trust Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/18/9c633d9995e11bf8607170ec9a4b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Oracle | [View](https://www.openjobs-ai.com/jobs/global-trust-advisor-united-states-135641404801024430) |
| Staff Software Engineer – User Identity, Messaging & Trust Infrastructure | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/8a/53918eff510582b74acb0ff511ce6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Quizlet | [View](https://www.openjobs-ai.com/jobs/staff-software-engineer-user-identity-messaging-trust-infrastructure-san-francisco-ca-135641404801024431) |
| Production Operator 1st & 2nd shift available | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/8d/e76be154592094de23849bed78daa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BAE Systems, Inc. | [View](https://www.openjobs-ai.com/jobs/production-operator-1st-2nd-shift-available-greenlawn-ny-135641404801024432) |
| Clinical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/41/81fb246bb80624a85671084db6517.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Advantage Behavioral Health | [View](https://www.openjobs-ai.com/jobs/clinical-therapist-yardley-pa-135641404801024433) |
| Accounting Consultant – Engagement Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/d0/aa75c241dba6e00699f9ff7a3dce5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CLA (CliftonLarsonAllen) | [View](https://www.openjobs-ai.com/jobs/accounting-consultant-engagement-director-west-hartford-ct-135641404801024434) |
| Renewals Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/46/1f4b876b0ba00582bbd6cd53af7f0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UL Solutions | [View](https://www.openjobs-ai.com/jobs/renewals-specialist-vancouver-wa-135641404801024435) |
| Environmental Field Technician - (Stack) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ec/878b35def0991cb6459e22c50b004.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Montrose Environmental Group | [View](https://www.openjobs-ai.com/jobs/environmental-field-technician-stack-auburn-wa-135641404801024436) |
| Direct Support Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/9d/79f0b46929b9fdcd3b849621cf917.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sevita | [View](https://www.openjobs-ai.com/jobs/direct-support-professional-old-orchard-beach-me-135641404801024437) |
| Osteopathic Core Faculty - Lancaster General Health Family Medicine Residency | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/22/09e99b3082b3fd5395bf331ebd02b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Penn Medicine Lancaster General Health | [View](https://www.openjobs-ai.com/jobs/osteopathic-core-faculty-lancaster-general-health-family-medicine-residency-lancaster-pa-135641404801024438) |
| Associate Dentist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/19/4465a98cb0783f45f5a2800940376.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aspen Dental | [View](https://www.openjobs-ai.com/jobs/associate-dentist-williston-vt-135641404801024439) |
| Physician Hospitalist - Thomas Memorial Hospital | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/00/1511322ed0675a3189328643615a3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WVU Medicine | [View](https://www.openjobs-ai.com/jobs/physician-hospitalist-thomas-memorial-hospital-south-charleston-wv-135641404801024440) |
| Wealth Management Private Banker | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/f1/d4e01801a0877ea2d864b32c1a98d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> United Community | [View](https://www.openjobs-ai.com/jobs/wealth-management-private-banker-brentwood-tn-135641404801024442) |
| Tax Principal - Banking and Specialty Finance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/d0/aa75c241dba6e00699f9ff7a3dce5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CLA (CliftonLarsonAllen) | [View](https://www.openjobs-ai.com/jobs/tax-principal-banking-and-specialty-finance-chicago-il-135641404801024443) |
| Comics & Superheroes Content Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/a3/4cbd4c3a59dcbeba8234609ea3edd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CBR | [View](https://www.openjobs-ai.com/jobs/comics-superheroes-content-writer-new-york-ny-135641404801024444) |
| Bloomberg Intelligence Digital Assets Company Research Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f1/70932743e65054b272ce3780bb908.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bloomberg | [View](https://www.openjobs-ai.com/jobs/bloomberg-intelligence-digital-assets-company-research-analyst-new-york-ny-135641404801024445) |
| Caregiver - Nama West DTA (Full Time) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/9d/79f0b46929b9fdcd3b849621cf917.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sevita | [View](https://www.openjobs-ai.com/jobs/caregiver-nama-west-dta-full-time-peoria-az-135641404801024446) |
| Tech Transfer Marketing Analyst -Technology Ventures | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/bb/0772f0e6d00ade574ba52b0eb55af.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cedars-Sinai | [View](https://www.openjobs-ai.com/jobs/tech-transfer-marketing-analyst-technology-ventures-california-united-states-135641404801024447) |
| Licensed Practical Nurse (LPN) - Physician Office-Gastroenterology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/46/79e609f5af0ee23f41c2c44408754.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bon Secours Mercy Health | [View](https://www.openjobs-ai.com/jobs/licensed-practical-nurse-lpn-physician-office-gastroenterology-greenville-sc-135641404801024448) |
| Manufacturing Electrical Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ea/ff5ae9a836c08bb57beaa701dc658.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Globus Medical | [View](https://www.openjobs-ai.com/jobs/manufacturing-electrical-engineer-memphis-tn-135641404801024449) |
| Plant Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/be/94272f60b113c9bc838e2076cd5a0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Standex Engraving Mold-Tech | [View](https://www.openjobs-ai.com/jobs/plant-manager-fraser-mi-135641404801024450) |
| Product Demonstrator Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/5d/7affe96fe46d9e9d7d04b434f7be5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Product Connections | [View](https://www.openjobs-ai.com/jobs/product-demonstrator-part-time-sarasota-fl-135641404801024451) |
| Director Product Management, Analytics | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/f9/cf2b82d2763938bc8e01e19edd5af.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Henry Schein One | [View](https://www.openjobs-ai.com/jobs/director-product-management-analytics-united-states-135641404801024452) |
| Internal Audit & Risk Manager – Insurance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/ae/adcdd10a3fc7fe87253316d11890d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Baker Tilly US | [View](https://www.openjobs-ai.com/jobs/internal-audit-risk-manager-insurance-philadelphia-pa-135641404801024453) |

<p align="center">
  <em>...and 711 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 16, 2026
</p>
