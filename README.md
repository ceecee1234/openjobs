<p align="center">
  <img src="https://img.shields.io/badge/jobs-795+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-568+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 568+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 349 |
| Healthcare | 203 |
| Management | 95 |
| Engineering | 76 |
| Sales | 31 |
| Finance | 27 |
| HR | 5 |
| Operations | 5 |
| Marketing | 4 |

**Top Hiring Companies:** Deloitte, Jacobs, Production Planning, Senior Helpers, KPMG US

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
│  │ Sitemap     │   │ (795+ jobs) │   │ (README + HTML)     │   │
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
- **And 568+ other companies**

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
  <em>Updated January 25, 2026 · Showing 200 of 795+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Licensed Practical Nurse VNA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/01/6b469c2071eef5856ef57a5cd3c19.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaleida Health | [View](https://www.openjobs-ai.com/jobs/licensed-practical-nurse-vna-cheektowaga-ny-127669660286976057) |
| International Tax and Transaction Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Transfer Pricing Senior | [View](https://www.openjobs-ai.com/jobs/international-tax-and-transaction-services-transfer-pricing-senior-fy26-minneapolis-mn-127669660286976058) |
| Nuclear Medicine Tech B | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/01/6b469c2071eef5856ef57a5cd3c19.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaleida Health | [View](https://www.openjobs-ai.com/jobs/nuclear-medicine-tech-b-olean-ny-127669660286976059) |
| Physical Therapy Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/bc/12f4787dfd22d584ae7a8a2c58f56.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Full-time | [View](https://www.openjobs-ai.com/jobs/physical-therapy-assistant-full-time-home-health-stoughton-wisconsin-watertown-wi-127669660286976060) |
| Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/5c/7c5e3d28748e958ecfbed0bc3e88f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Special Education | [View](https://www.openjobs-ai.com/jobs/teacher-special-education-leap-2025-2026-sy-norwalk-ct-127669660286976061) |
| Senior Data Scientist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/6b/3931b9959c927df4fc65fdee94b07.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Copeland | [View](https://www.openjobs-ai.com/jobs/senior-data-scientist-sidney-oh-127669660286976062) |
| Call Center Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/cf/c59b276e4dbe20107ce6f5e348760.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MCI | [View](https://www.openjobs-ai.com/jobs/call-center-representative-killeen-tx-127669660286976064) |
| Data Center Construction Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/f7/72753bacf4cbd1ea1f6cdbea2cd1c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Blue Signal Search | [View](https://www.openjobs-ai.com/jobs/data-center-construction-lead-texas-united-states-127669660286976065) |
| Call Center Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/cf/c59b276e4dbe20107ce6f5e348760.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MCI | [View](https://www.openjobs-ai.com/jobs/call-center-representative-hinesville-ga-127669660286976066) |
| Senior Data Scientist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/6b/3931b9959c927df4fc65fdee94b07.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Copeland | [View](https://www.openjobs-ai.com/jobs/senior-data-scientist-kennesaw-ga-127669660286976067) |
| NURSING CARE ASSISTANT - STATE CERTIFIED | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/13/5a7078f2d3c7eb0061f5eb1ace37c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Covenant HealthCare | [View](https://www.openjobs-ai.com/jobs/nursing-care-assistant-state-certified-saginaw-mi-127669660286976068) |
| Physical Therapist Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a6/e10e127898922fc0aa516d6b3449c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Talented Medical Solutions | [View](https://www.openjobs-ai.com/jobs/physical-therapist-assistant-tallahassee-fl-127669660286976069) |
| Licensed Practical Nurse – GTE (LPN) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a6/e10e127898922fc0aa516d6b3449c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Talented Medical Solutions | [View](https://www.openjobs-ai.com/jobs/licensed-practical-nurse-gte-lpn-fertile-mn-127669660286976070) |
| LPN – Geriatric/Extended Care (LPN GTE) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a6/e10e127898922fc0aa516d6b3449c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Talented Medical Solutions | [View](https://www.openjobs-ai.com/jobs/lpn-geriatricextended-care-lpn-gte-fertile-mn-127669660286976071) |
| Crane Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/62/cc545d0b52f0b1fdec81ce9604b48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sims Metal | [View](https://www.openjobs-ai.com/jobs/crane-operator-philadelphia-pa-127669660286976072) |
| Outpatient Registered Nurse - RN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/0d/cd8797fca6888b7f7f26d25e6624d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fresenius Medical Care | [View](https://www.openjobs-ai.com/jobs/outpatient-registered-nurse-rn-lebanon-nh-127669660286976073) |
| Travel Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a6/e10e127898922fc0aa516d6b3449c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Talented Medical Solutions | [View](https://www.openjobs-ai.com/jobs/travel-physical-therapist-sarasota-fl-127669660286976074) |
| Occupational Therapist Assistant (COTA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a6/e10e127898922fc0aa516d6b3449c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Talented Medical Solutions | [View](https://www.openjobs-ai.com/jobs/occupational-therapist-assistant-cota-galesburg-il-127669660286976075) |
| Apprentice Electrician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/0d/bfe3bee4f439d00e9f796917755d0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Generator | [View](https://www.openjobs-ai.com/jobs/apprentice-electrician-los-angeles-ca-127669660286976076) |
| Rapid Response Paramedic (FEMA Support) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ae/f2c0bba4c170a9f498e708c2a9e74.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dentrust Optimized Care Solutions | [View](https://www.openjobs-ai.com/jobs/rapid-response-paramedic-fema-support-ruidoso-nm-127669660286976077) |
| Physician - General Hematology Oncology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/25/751eb4911b57c285189e49da3b389.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hawaii Pacific Health | [View](https://www.openjobs-ai.com/jobs/physician-general-hematology-oncology-lihue-hi-127669660286976078) |
| Data Product Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Senior | [View](https://www.openjobs-ai.com/jobs/data-product-management-senior-financial-services-consulting-nyc-charlotte-dallas-charlotte-nc-127669660286976079) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-san-mateo-ca-127669660286976080) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-providence-ri-127669660286976081) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-houston-tx-127669660286976082) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-arlington-va-127669660286976083) |
| Family Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/7a/203fd5aab85616eec3c2456b48cfb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Youth Advocate Programs, Inc. | [View](https://www.openjobs-ai.com/jobs/family-coordinator-fort-worth-tx-127669660286976084) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-rochester-ny-127669660286976085) |
| Engineering Manager – Indexing and Search Systems | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/1c/5944a9b3b9555aeff5a8e3635a314.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wayve | [View](https://www.openjobs-ai.com/jobs/engineering-manager-indexing-and-search-systems-sunnyvale-ca-127669660286976086) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-jericho-ny-127669660286976087) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-charleston-wv-127669660286976088) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-new-brunswick-nj-127669660286976089) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-las-vegas-nv-127669660286976090) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-tallahassee-fl-127669660286976091) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-irvine-ca-127669660286976092) |
| Data Product Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Senior | [View](https://www.openjobs-ai.com/jobs/data-product-management-senior-financial-services-consulting-nyc-charlotte-dallas-dallas-tx-127669660286976093) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-iselin-nj-127669660286976094) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-akron-oh-127669660286976095) |
| SAP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production Planning | [View](https://www.openjobs-ai.com/jobs/sap-production-planning-pp-senior-consulting-location-open-hartford-ct-127669660286976096) |
| Data Product Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Senior | [View](https://www.openjobs-ai.com/jobs/data-product-management-senior-financial-services-consulting-nyc-charlotte-dallas-new-york-ny-127669660286976097) |
| RN Unit Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4c/19ac66185603acd5c3e2a2e5fabd3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Allure Group | [View](https://www.openjobs-ai.com/jobs/rn-unit-manager-new-york-ny-127669660286976098) |
| Manufacturing Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/66/3259a8e1ec477c22a4ba760ee55af.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Legrand, North America | [View](https://www.openjobs-ai.com/jobs/manufacturing-engineer-union-oh-127669660286976099) |
| Accounting & Reporting Advisory Experienced Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/0e/c4f94e12750f4805fb0664d062246.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BDO USA | [View](https://www.openjobs-ai.com/jobs/accounting-reporting-advisory-experienced-senior-associate-san-jose-ca-127669660286976100) |
| HCPA Medical Social Worker | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/01/6b469c2071eef5856ef57a5cd3c19.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaleida Health | [View](https://www.openjobs-ai.com/jobs/hcpa-medical-social-worker-bradford-pa-127669660286976101) |
| Lead Relay Test Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/65/7b844ed41966eb374ba12c8ec2f5b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TRC Companies, Inc. | [View](https://www.openjobs-ai.com/jobs/lead-relay-test-technician-springfield-ma-127669660286976102) |
| Procurement Planning/Compliance Manager Japanese/English speaking required | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/f1/765462d24476b7e4281c9b2cd87ad.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Panasonic North America | [View](https://www.openjobs-ai.com/jobs/procurement-planningcompliance-manager-japaneseenglish-speaking-required-torrance-ca-127669660286976103) |
| Learning Behavior Specialist (Structured Learning) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/c9/9e4da8524fc228c4bc1766d6e607d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Naperville Community Unit School District 203 | [View](https://www.openjobs-ai.com/jobs/learning-behavior-specialist-structured-learning-naperville-il-127669660286976104) |
| Clinical Program Supervisor (Palos Hills) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/a9/dce534e8f983560779a297e047018.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Metropolitan Family Services | [View](https://www.openjobs-ai.com/jobs/clinical-program-supervisor-palos-hills-palos-hills-il-127669660286976105) |
| City of Santa Clara - Volunteer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/2d/8f3c24f3bda92221ddb6549434ea2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of Santa Clara | [View](https://www.openjobs-ai.com/jobs/city-of-santa-clara-volunteer-santa-clara-ca-127669660286976106) |
| Psychiatric Staff Nurse - 50% Integrated Health and Aging Program (IHAP, 12th Floor) Day/Evening 8 hour shifts | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/da/a7ca3bb8102d1bc044ecbcce29284.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UPMC | [View](https://www.openjobs-ai.com/jobs/psychiatric-staff-nurse-50-integrated-health-and-aging-program-ihap-12th-floor-dayevening-8-hour-shifts-pittsburgh-pa-127669660286976107) |
| Sales Executive - Business Insurance, Agribusiness Practice | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/59/6e84f048481bd7ad601fe05985490.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Marsh McLennan Agency | [View](https://www.openjobs-ai.com/jobs/sales-executive-business-insurance-agribusiness-practice-richland-wa-127669660286976108) |
| Medical Director or Attending Physician - Sullivan, IL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/c6/e257f55d3ae4936e1c14fa1d806b3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Theoria Medical | [View](https://www.openjobs-ai.com/jobs/medical-director-or-attending-physician-sullivan-il-sullivan-il-127669660286976109) |
| Postal Finance Clerk (AUAB contingent upon award) - Qatar | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/83/6b4bf92e36b7cd8bc3dff4fa7b2b2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Chenega MIOS SBU | [View](https://www.openjobs-ai.com/jobs/postal-finance-clerk-auab-contingent-upon-award-qatar-minot-afb-nd-127669660286976110) |
| Patient Access Specialist (Full-Time Swing Shift, 2P-2A) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/33/a06d298090bc338328b86f15b370b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Emerus Holdings, Inc. | [View](https://www.openjobs-ai.com/jobs/patient-access-specialist-full-time-swing-shift-2p-2a-knox-city-tx-127669660286976111) |
| SHEET METAL WORKER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/05/960da20f75f493bb4410d45a8568a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> County of Los Angeles | [View](https://www.openjobs-ai.com/jobs/sheet-metal-worker-los-angeles-ca-127669660286976112) |
| MANAGER III, FACILITIES OPERATIONS AND CRAFTS | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/05/960da20f75f493bb4410d45a8568a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> County of Los Angeles | [View](https://www.openjobs-ai.com/jobs/manager-iii-facilities-operations-and-crafts-los-angeles-ca-127669660286976113) |
| MENTAL HEALTH PROMOTER / TEMPORARY | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/05/960da20f75f493bb4410d45a8568a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> County of Los Angeles | [View](https://www.openjobs-ai.com/jobs/mental-health-promoter-temporary-los-angeles-ca-127669660286976114) |
| ME00441-Mid-Senior System Administrator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/56/44e38facef0961c7b9978f87718a2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Momentum Engineering, Inc. | [View](https://www.openjobs-ai.com/jobs/me00441-mid-senior-system-administrator-annapolis-junction-md-127669660286976115) |
| Bloomfield \| ABI Home CNA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/50/52e61643851fc65b6a2246e3816ef.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ABI RESOURCES | [View](https://www.openjobs-ai.com/jobs/bloomfield-abi-home-cna-bloomfield-ct-127669660286976116) |
| Bilingual Behavioral Assistant (Union County) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/8c/68a7c61a87abe2e6f1fbf29d4248a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Neuropath Behavioral Healthcare | [View](https://www.openjobs-ai.com/jobs/bilingual-behavioral-assistant-union-county-elizabeth-nj-127669660286976117) |
| Batching Technician I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/56/b82c301bef07b7f05cbde013cb7c2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Multipack | [View](https://www.openjobs-ai.com/jobs/batching-technician-i-shreveport-la-127669660286976118) |
| Licensed Professional Counselor or Licensed Marriage and Family Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/50/5a89940b63659a284e3cb7973b7cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Eventus WholeHealth | [View](https://www.openjobs-ai.com/jobs/licensed-professional-counselor-or-licensed-marriage-and-family-therapist-kokomo-in-127669660286976119) |
| SkillBridge EMT - West Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-west-region-multiple-locations-albuquerque-nm-127669660286976120) |
| BSA - AI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/fa/6be22eaf1f9c91942324a401ae982.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> J&M Group | [View](https://www.openjobs-ai.com/jobs/bsa-ai-irving-tx-127669660286976121) |
| Marketing Analyst/Manager T3 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b7/247606d865f6e49b1734023c38836.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Netpace Inc | [View](https://www.openjobs-ai.com/jobs/marketing-analystmanager-t3-newtown-square-pa-127669660286976122) |
| Associate Vice President of Internal Human Resources, Communities of Excellence | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/a0/dfcd0a9dfcbdd5229bdcb3aedae45.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AZ, GA | [View](https://www.openjobs-ai.com/jobs/associate-vice-president-of-internal-human-resources-communities-of-excellence-az-ga-on-site-chandler-az-127669660286976123) |
| SkillBridge EMT - South Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-south-region-multiple-locations-knoxville-tn-127669660286976124) |
| SkillBridge EMT - South Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-south-region-multiple-locations-jackson-ms-127669660286976125) |
| SkillBridge EMT - North Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-north-region-multiple-locations-mount-vernon-ny-127669660286976126) |
| SkillBridge EMT - South Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-south-region-multiple-locations-stone-mountain-ga-127669660286976127) |
| SkillBridge EMT - West Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-west-region-multiple-locations-phoenix-az-127669660286976128) |
| SkillBridge EMT - West Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-west-region-multiple-locations-las-vegas-nv-127669660286976129) |
| LPC, LCSW or LMFT Social Worker (License Required) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f6/d0ff9cedb0f6e48e63d6a2327e699.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RKM Primary Care | [View](https://www.openjobs-ai.com/jobs/lpc-lcsw-or-lmft-social-worker-license-required-springfield-la-127669660286976130) |
| Sr. IT Service Management Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/4d/e2bd44988f66062b86c94b6d6c770.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PlanIT Group, LLC | [View](https://www.openjobs-ai.com/jobs/sr-it-service-management-specialist-raleigh-nc-127669660286976131) |
| LPC, LCSW or LMFT Social Worker (License Required) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f6/d0ff9cedb0f6e48e63d6a2327e699.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RKM Primary Care | [View](https://www.openjobs-ai.com/jobs/lpc-lcsw-or-lmft-social-worker-license-required-livingston-la-127669660286976132) |
| SkillBridge EMT - North Region (Multiple Locations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/43/5bbf704b6454669f95c8a50d11fbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Medical Response | [View](https://www.openjobs-ai.com/jobs/skillbridge-emt-north-region-multiple-locations-manchester-nh-127669660286976133) |
| Family Medicine APP (NP/PA) - Family Medicine | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/88/8e77cd117a2e189461b4c4b14cb38.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pittsboro at UNC Health | [View](https://www.openjobs-ai.com/jobs/family-medicine-app-nppa-family-medicine-at-pittsboro-pittsboro-nc-127669660286976134) |
| Industrial Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/0a/1d21a4f69920f2936d83ac7b3838c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> General Atomics | [View](https://www.openjobs-ai.com/jobs/industrial-mechanic-tupelo-ms-127669660286976135) |
| Sr Aerothermal Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/ac/c99eb2fceac8e027fbc1e6d60a98d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Relativity Space | [View](https://www.openjobs-ai.com/jobs/sr-aerothermal-engineer-long-beach-ca-127669660286976136) |
| Electronics Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/4d/e2bd44988f66062b86c94b6d6c770.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PlanIT Group, LLC | [View](https://www.openjobs-ai.com/jobs/electronics-technician-ventura-ca-127669660286976137) |
| Aerodynamics Engineer II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/ac/c99eb2fceac8e027fbc1e6d60a98d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Relativity Space | [View](https://www.openjobs-ai.com/jobs/aerodynamics-engineer-ii-long-beach-ca-127669660286976138) |
| Registered Nurse Transitional Nursery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/1d/825a669c0b9d37b230497db9f1932.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Las Palmas Medical Center | [View](https://www.openjobs-ai.com/jobs/registered-nurse-transitional-nursery-el-paso-tx-127669660286976139) |
| Neonatologist - Medical Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/1a/f680ddc36382ba898244ff71a83ec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pediatrix Medical Group | [View](https://www.openjobs-ai.com/jobs/neonatologist-medical-director-athens-ga-127669660286976140) |
| IT Procurement Specialist (2908*) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/78/158747ca683d1a6305f56dc737a58.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PSI Pax, Inc. | [View](https://www.openjobs-ai.com/jobs/it-procurement-specialist-2908-dahlgren-va-127669660286976141) |
| Systems Administrator (Windows) (2906) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/78/158747ca683d1a6305f56dc737a58.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PSI Pax, Inc. | [View](https://www.openjobs-ai.com/jobs/systems-administrator-windows-2906-dahlgren-va-127669660286976143) |
| Program Manager (2909*) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/78/158747ca683d1a6305f56dc737a58.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PSI Pax, Inc. | [View](https://www.openjobs-ai.com/jobs/program-manager-2909-dahlgren-va-127669660286976144) |
| Senior Data Analyst (2911*) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/78/158747ca683d1a6305f56dc737a58.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PSI Pax, Inc. | [View](https://www.openjobs-ai.com/jobs/senior-data-analyst-2911-dahlgren-va-127669660286976145) |
| FINANCE MANAGER - AUTOMOTIVE
CARDINALEWAY VOLKSWAGEN - CORONA at Cardinale Automotive Group | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/68/acda7aacf886193beda0ec8c11bf7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> - | [View](https://www.openjobs-ai.com/jobs/finance-manager-automotive-cardinaleway-volkswagen-corona-corona-ca-127669660286976146) |
| Document Control Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/5e/7c03b13aa2f87c8bfd764276d061c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> R.E. Darling Company Inc. | [View](https://www.openjobs-ai.com/jobs/document-control-specialist-tucson-az-127669660286976147) |
| Director, CFO Services (OPEN TO ALL US LOCATIONS) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/27/1f677024528382e2f1d390551f7f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alvarez & Marsal | [View](https://www.openjobs-ai.com/jobs/director-cfo-services-open-to-all-us-locations-charlotte-nc-127670000025600000) |
| Campaign Manager (Amazon Ads) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/ce/7d9bf9e9aacabba3cfa8c7628a5a4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NeaMob Ltd | [View](https://www.openjobs-ai.com/jobs/campaign-manager-amazon-ads-georgia-127670000025600001) |
| Live In Caregiver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/e4/ccdae5fae24543a674023f9a7d0a6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Home Instead | [View](https://www.openjobs-ai.com/jobs/live-in-caregiver-granger-in-127670000025600002) |
| Clinical Registered Nurse II (Lynchburg General Hospital, Med Surg Units) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/92/1be8c595d57c7bc8da0dc0b667962.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Centra Health | [View](https://www.openjobs-ai.com/jobs/clinical-registered-nurse-ii-lynchburg-general-hospital-med-surg-units-lynchburg-va-127670000025600003) |
| Welder | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/23/366fac5f9694c3db512f50f5c8096.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 2nd Shift | [View](https://www.openjobs-ai.com/jobs/welder-2nd-shift-port-washington-wi-port-washington-wi-127670000025600004) |
| DAYCARE WORKER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/28/752de89d38cd1183b96507ee7bd30.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Connally ISD | [View](https://www.openjobs-ai.com/jobs/daycare-worker-waco-tx-127670000025600005) |
| Registered Nurse Adult Med | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/63/bf5c4caf1b0f406d3f14864c3b95d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brown University Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-adult-med-providence-ri-127670000025600006) |
| Industrial Waterblast & Vacuum Foreman | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/8e/fd65d589039ae6811fb3ddb68ee2f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> O6 Environmental Services | [View](https://www.openjobs-ai.com/jobs/industrial-waterblast-vacuum-foreman-st-louis-mo-127670000025600007) |
| Assistant Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/b1/462086b23461d6ba9c51c2ad01a45.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gardens Care Senior Living | [View](https://www.openjobs-ai.com/jobs/assistant-manager-northglenn-co-127670000025600008) |
| System Product Manager (27614) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/49/52f62b1cf4f7c31ea09b45352e5ec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Supermicro | [View](https://www.openjobs-ai.com/jobs/system-product-manager-27614-san-jose-ca-127670000025600009) |
| Service Manager - Lake Worth, FL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/service-manager-lake-worth-fl-lake-worth-fl-127670000025600010) |
| Theater General Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/29/c381032729a0173f7de49a0eb6cf5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ponca City Development Authority | [View](https://www.openjobs-ai.com/jobs/theater-general-manager-ponca-city-ok-127670000025600011) |
| REGISTERED NURSE, Operating Room -  Part Time Days | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/12/d6ca1aaaa2d12f259f4403dc0384a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northern Nevada Health System | [View](https://www.openjobs-ai.com/jobs/registered-nurse-operating-room-part-time-days-sparks-nv-127670000025600012) |
| Wire Bonder Worker - 2nd Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/46/ea72c850081dc761067a3e3961613.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Raytheon | [View](https://www.openjobs-ai.com/jobs/wire-bonder-worker-2nd-shift-goleta-ca-127670000025600013) |
| Registered Nurse / RN ER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/47/c42e4c52d67f123456c5ba567b3d4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UT Health East Texas | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-er-pittsburg-tx-127670000025600014) |
| Licensed Mental Health Counselor (LMHC) - Telehealth | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/80/c60bbe7fc6d1479bab3aa452f1e18.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brightside Health | [View](https://www.openjobs-ai.com/jobs/licensed-mental-health-counselor-lmhc-telehealth-melbourne-ia-127670000025600015) |
| Associate Principal, Sourcing & Procurement | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/f0/4b700da1d8c0641b4be9bfdd83d20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Options Clearing Corporation (OCC) | [View](https://www.openjobs-ai.com/jobs/associate-principal-sourcing-procurement-chicago-il-127670000025600016) |
| Qmap | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/b1/462086b23461d6ba9c51c2ad01a45.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gardens Care Senior Living | [View](https://www.openjobs-ai.com/jobs/qmap-aurora-co-127670000025600017) |
| Director, Client Solutions | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/85/a26525de97c4f68097054c5efe946.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alloy.ai | [View](https://www.openjobs-ai.com/jobs/director-client-solutions-denver-co-127670000025600019) |
| Veterinary Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/bb/d560713f843e2b561976216334e05.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AmeriVet Veterinary Partners | [View](https://www.openjobs-ai.com/jobs/veterinary-technician-middle-village-ny-127670000025600020) |
| Underwriter III | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/92/23884123060644bf5c6ac282df208.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AmeriHome Mortgage Company, LLC | [View](https://www.openjobs-ai.com/jobs/underwriter-iii-texas-united-states-127670000025600021) |
| Premium Audit Auditor II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/1e/795edcddc17792f1fe5fc1785d77e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Zurich North America | [View](https://www.openjobs-ai.com/jobs/premium-audit-auditor-ii-alabama-united-states-127670000025600022) |
| Speech Language Pathologist, AAMC, Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/ff/9cb374cfbef4fc25bbccc6a4f08a2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Self Regional Healthcare | [View](https://www.openjobs-ai.com/jobs/speech-language-pathologist-aamc-part-time-abbeville-sc-127670000025600023) |
| Outpatient Radiologic Tech | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/d6/84b827afd56a48ed9de0ad75e8169.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Memorial Health | [View](https://www.openjobs-ai.com/jobs/outpatient-radiologic-tech-springfield-il-127670000025600024) |
| Licensed Psychologist- Psypact Certified | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/37/c76b129b7d2d6cbcb5d64831b6179.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vida Health | [View](https://www.openjobs-ai.com/jobs/licensed-psychologist-psypact-certified-united-states-127670000025600025) |
| Development Coordinator - Full Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/00/f9097ae0140809b3de599f96f6248.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OakBend Medical Center | [View](https://www.openjobs-ai.com/jobs/development-coordinator-full-time-richmond-tx-127670000025600026) |
| Clinical Supervisor/BCBA Remote | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/40/bc23e837227ff037d681f2315ea55.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Childwise ABA | [View](https://www.openjobs-ai.com/jobs/clinical-supervisorbcba-remote-ohio-united-states-127670000025600027) |
| 4th Semester Clinical Partnership | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/de/3e4cdb26f47ca6217738481ebe281.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Freeman Health System | [View](https://www.openjobs-ai.com/jobs/4th-semester-clinical-partnership-joplin-mo-127670000025600028) |
| Sr. Director, Data Science, Patient Identification | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/21/113136b6979736a2f9fd3827b94b0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BridgeBio | [View](https://www.openjobs-ai.com/jobs/sr-director-data-science-patient-identification-san-francisco-bay-area-127670000025600029) |
| Senior Engineering Manager, AI Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/d9/03ccd68212f85fc2e700e4733e52f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Adobe | [View](https://www.openjobs-ai.com/jobs/senior-engineering-manager-ai-assistant-san-jose-ca-127670000025600030) |
| Administrative Coordinator / Behavioral Health / Vance County | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/eb/d1a15e7e900e93ce4597fe4c04bab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RHA Health Services, LLC | [View](https://www.openjobs-ai.com/jobs/administrative-coordinator-behavioral-health-vance-county-henderson-nc-127670000025600031) |
| Patient Care Technician I, NRS, AAMC, Resource Pool, Nights | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/ff/9cb374cfbef4fc25bbccc6a4f08a2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Self Regional Healthcare | [View](https://www.openjobs-ai.com/jobs/patient-care-technician-i-nrs-aamc-resource-pool-nights-abbeville-sc-127670000025600032) |
| Intake Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/db/9a87c80f7523400d1adbb60403099.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trilogy | [View](https://www.openjobs-ai.com/jobs/intake-specialist-chicago-il-127670000025600033) |
| Customer Success Manager- Power & Renewables - 25434 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/e7/cfcae0f9ad1a4803815e1683a6f58.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Enverus | [View](https://www.openjobs-ai.com/jobs/customer-success-manager-power-renewables-25434-austin-tx-127670000025600034) |
| Senior Applications Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/97/3fdfec10c6f726b11f273488ad009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Penn Medicine, University of Pennsylvania Health System | [View](https://www.openjobs-ai.com/jobs/senior-applications-manager-philadelphia-pa-127670000025600035) |
| Sales Counselor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/07/53d2276fa75c06c6a855718f24a7e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Everstory Partners | [View](https://www.openjobs-ai.com/jobs/sales-counselor-harrisburg-pa-127670000025600036) |
| Renewables National Accounts Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/ef/54287cbb4d1e38c10c476063fec87.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Integrated Power Services | [View](https://www.openjobs-ai.com/jobs/renewables-national-accounts-manager-abilene-tx-127670000025600037) |
| Associate Director, Data Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/63/7084f645d8d953bb57a7ef5348be4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rigel Pharmaceuticals Inc. | [View](https://www.openjobs-ai.com/jobs/associate-director-data-management-united-states-127670000025600038) |
| Associate Veterinarian | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/20/6972ecd2543043af3415a2cbbe9d4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> VCA Animal Hospitals | [View](https://www.openjobs-ai.com/jobs/associate-veterinarian-plano-tx-127670000025600039) |
| Nuclear Medicine Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/63/638a734e078796634fab1eea3d138.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Essentia Health | [View](https://www.openjobs-ai.com/jobs/nuclear-medicine-technologist-virginia-mn-127670000025600040) |
| Senior Financial Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/ca/b63042aa70eab88dff21426b09eda.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Adoration Health | [View](https://www.openjobs-ai.com/jobs/senior-financial-analyst-louisville-ky-127670000025600041) |
| PCU RN - Progressive Care Unit Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/1c/31bd8eeafea3d68e6b79fba75e6d7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MercyOne | [View](https://www.openjobs-ai.com/jobs/pcu-rn-progressive-care-unit-registered-nurse-clinton-ia-127670000025600042) |
| Physcian | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/f9/46851d20d169306dbd09f31601f20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tele-Neurohospital Medicine | [View](https://www.openjobs-ai.com/jobs/physcian-tele-neurohospital-medicine-remote-tn-c-nashville-tn-127670000025600043) |
| Commercial Claims Adjuster, TPA Oversight | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/21/daefdb424e954c6163d3a4d292fd5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AIG | [View](https://www.openjobs-ai.com/jobs/commercial-claims-adjuster-tpa-oversight-chicago-il-127670000025600044) |
| Senior Lab Researcher - Abbott Lab | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/4a/316314f4f452e1f1cf3ca62452e2f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> National Jewish Health | [View](https://www.openjobs-ai.com/jobs/senior-lab-researcher-abbott-lab-denver-co-127670000025600045) |
| Caregiver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/10/4a92b8abda5169c6990f642515288.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brookdale | [View](https://www.openjobs-ai.com/jobs/caregiver-alliance-oh-127670000025600046) |
| Advanced Practice Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/35/1f4f484abe7647116dc9374ed11ca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hunterdon Health | [View](https://www.openjobs-ai.com/jobs/advanced-practice-nurse-flemington-nj-127670000025600047) |
| Tech Level 1 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/8e/ef491dbb2aa315399bb3169e870df.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Simpay | [View](https://www.openjobs-ai.com/jobs/tech-level-1-trevose-pa-127670000025600048) |
| CT Tech-Eligible, Full-Time, Day Shift (7am-7pm Fri-Sun) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/5c/dc5bde0629db186a57cefe96e56f5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Prisma Health | [View](https://www.openjobs-ai.com/jobs/ct-tech-eligible-full-time-day-shift-7am-7pm-fri-sun-greenville-sc-127670000025600049) |
| Behavioral Health Associate (7A-3P)-Adolescent Unit | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/a8/3befa63dccc692a923fcd820d49f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crestwyn Behavioral Health | [View](https://www.openjobs-ai.com/jobs/behavioral-health-associate-7a-3p-adolescent-unit-memphis-tn-127670000025600050) |
| DSST - Analyzing and Interpreting English Literature | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/bd/f2fcc11fe013177f202839b2811fe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Prometric | [View](https://www.openjobs-ai.com/jobs/dsst-analyzing-and-interpreting-english-literature-united-states-127670000025600051) |
| Warehouse Operations Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/dd/09f476179e1f24467b2d500e3799c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Primis Bank | [View](https://www.openjobs-ai.com/jobs/warehouse-operations-specialist-frisco-tx-127670000025600052) |
| UNIV | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/16/eb7f343d8c9142856d7ab257ea40a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Research Laboratory Manager | [View](https://www.openjobs-ai.com/jobs/univ-research-laboratory-manager-pharmacology-immunology-charleston-sc-127670000025600053) |
| Manufacturing Engineer I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/70/9588a50d6fc48d572aba65a4bcdef.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Terex Corporation | [View](https://www.openjobs-ai.com/jobs/manufacturing-engineer-i-moses-lake-wa-127670000025600054) |
| Patient Safety Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/35/1f4f484abe7647116dc9374ed11ca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hunterdon Health | [View](https://www.openjobs-ai.com/jobs/patient-safety-assistant-flemington-nj-127670000025600055) |
| CNA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/91/59d977876480e94119a976fd1c393.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Catholic Health | [View](https://www.openjobs-ai.com/jobs/cna-smithtown-ny-127670000025600056) |
| Technology Co-op - Spring 2026 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/7e/2b153d432799d6d05995c6314a74e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Salas O'Brien | [View](https://www.openjobs-ai.com/jobs/technology-co-op-spring-2026-atlanta-ga-127670000025600057) |
| DSST - Introduction to Psychology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/bd/f2fcc11fe013177f202839b2811fe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Prometric | [View](https://www.openjobs-ai.com/jobs/dsst-introduction-to-psychology-united-states-127670000025600058) |
| Medication Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/10/4a92b8abda5169c6990f642515288.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brookdale | [View](https://www.openjobs-ai.com/jobs/medication-technician-dublin-oh-127670000025600060) |
| Medical Equipment Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/d6/1112a2a66189f17b39e705f16faf7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AdaptHealth | [View](https://www.openjobs-ai.com/jobs/medical-equipment-technician-fife-wa-127670000025600061) |
| Clinical Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/5e/134b1957c206a3d9efdc6c377b927.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hillcrest Children & Family Center | [View](https://www.openjobs-ai.com/jobs/clinical-director-washington-dc-127670000025600062) |
| Respiratory Therapist DT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/91/ec225e7a9a1b4d182dbbcb14cb21f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Naples Comprehensive Health | [View](https://www.openjobs-ai.com/jobs/respiratory-therapist-dt-naples-fl-127670000025600063) |
| Teachers Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/35/1f4f484abe7647116dc9374ed11ca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hunterdon Health | [View](https://www.openjobs-ai.com/jobs/teachers-assistant-flemington-nj-127670000025600064) |
| Clerical Assistant - Coronary Care Unit (CCU) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/91/59d977876480e94119a976fd1c393.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Catholic Health | [View](https://www.openjobs-ai.com/jobs/clerical-assistant-coronary-care-unit-ccu-smithtown-ny-127670000025600065) |
| Entry Level Electrical Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/7e/2b153d432799d6d05995c6314a74e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Salas O'Brien | [View](https://www.openjobs-ai.com/jobs/entry-level-electrical-designer-raleigh-nc-127670000025600066) |
| Senior Staff Machine Learning Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/df/acd88bfd876073c0f0ad9a22e3f87.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Patreon | [View](https://www.openjobs-ai.com/jobs/senior-staff-machine-learning-engineer-san-francisco-ca-127670000025600067) |
| Warehouse Technician (driving) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/d6/1112a2a66189f17b39e705f16faf7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AdaptHealth | [View](https://www.openjobs-ai.com/jobs/warehouse-technician-driving-everett-wa-127670000025600068) |
| Veterinary Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/20/6972ecd2543043af3415a2cbbe9d4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> VCA Animal Hospitals | [View](https://www.openjobs-ai.com/jobs/veterinary-assistant-costa-mesa-ca-127670000025600069) |
| Maintenance Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/9a/644bc2d84d4863b879fc767c87be8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IDE Technologies | [View](https://www.openjobs-ai.com/jobs/maintenance-planner-santa-barbara-ca-127670000025600070) |
| SERVER A03 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/4c/363254dc9759fb8a40598a2a9abbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NAVWAR | [View](https://www.openjobs-ai.com/jobs/server-a03-twentynine-palms-ca-127670000025600071) |
| Branch Service Supervisor or Senior - NW Albany | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/ee/7d5af45d395226ac8d6aa682f6518.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Synovus | [View](https://www.openjobs-ai.com/jobs/branch-service-supervisor-or-senior-nw-albany-albany-ga-127670000025600072) |
| Shift Miller - Camp Hill, PA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/09/c600fddc573f117449b3723f23d64.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ADM | [View](https://www.openjobs-ai.com/jobs/shift-miller-camp-hill-pa-camp-hill-pa-127670000025600073) |
| Associate Veterinarian | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/20/6972ecd2543043af3415a2cbbe9d4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> VCA Animal Hospitals | [View](https://www.openjobs-ai.com/jobs/associate-veterinarian-mesa-az-127670000025600074) |
| Client Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/0a/68092da0b98a7adb6ae41c18bd2dc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Baird | [View](https://www.openjobs-ai.com/jobs/client-specialist-mill-valley-ca-127670000025600075) |
| Marketing Specialist - C&S | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/59/7442c4163b564473fc8ade615afb1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Central Garden & Pet | [View](https://www.openjobs-ai.com/jobs/marketing-specialist-cs-franklin-wi-127670000025600076) |
| Occupational Therapist (Director of Rehab) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/2d/43c84bd65d8e3a606524ed756f962.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Heritage Manor Care | [View](https://www.openjobs-ai.com/jobs/occupational-therapist-director-of-rehab-santa-ana-ca-127670000025600077) |
| Senior SEC Reporting Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/46/13f891998a5332e9d4ffe2fb183c6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Confidential Careers | [View](https://www.openjobs-ai.com/jobs/senior-sec-reporting-analyst-oakbrook-terrace-il-127670000025600078) |
| Registered Nurse RN - All Shifts | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/ca/4e1f8f810ad85edb1943facf585ce.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Futurecare Associates, Inc. | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-all-shifts-cold-spring-ky-127670000025600079) |
| Host (Monday-Friday 11am-7:30) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/06/dc98a63c85fb1d4db11844f645f82.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crossover Health | [View](https://www.openjobs-ai.com/jobs/host-monday-friday-11am-730-menlo-park-ca-127670000025600080) |
| Optometrist (OD) - Full Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/6f/b9effc53a71bbd110d74e3c304269.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MyEyeDr. | [View](https://www.openjobs-ai.com/jobs/optometrist-od-full-time-charlottesville-va-127670000025600081) |
| Computer Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/cd/a0cf3ff7bea7cc872b40f05e89c98.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rich Township High School District 227 | [View](https://www.openjobs-ai.com/jobs/computer-technician-olympia-fields-il-127670000025600082) |
| 25-26 PT Prevocational Math Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/ec/9fb9393701ed2c5c5c0f8c1b08c48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Somerville Public Schools | [View](https://www.openjobs-ai.com/jobs/25-26-pt-prevocational-math-teacher-somerville-ma-127670000025600083) |
| Surgical Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/1e/259bfc254959459aebc14dc83a1e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Compass Surgical Partners | [View](https://www.openjobs-ai.com/jobs/surgical-technologist-center-point-la-127670000025600084) |
| Registered Nurse (RN) Intermediate Care/Step Down Unit | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/f6/4ad0a29a33a64fc7bfe57e8ad6601.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sentara Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-intermediate-carestep-down-unit-virginia-beach-va-127670000025600085) |
| QEI (Elevator Inspector)- Portland, ME | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/49/27a79c4b101c9b81226a0f7d2122f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bureau Veritas Group | [View](https://www.openjobs-ai.com/jobs/qei-elevator-inspector-portland-me-portland-me-127670000025600086) |
| Behavior Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/51/ebb4b74a4ec805d9288eb5884d341.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Total Spectrum, LLC | [View](https://www.openjobs-ai.com/jobs/behavior-technician-farmington-mi-127670000025600087) |
| Travel Registered Nurse Med Surg / Telemetry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/1b/4db9347e2907b68ce94537a0348b9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Coast Medical Service | [View](https://www.openjobs-ai.com/jobs/travel-registered-nurse-med-surg-telemetry-rochester-ny-127670000025600088) |
| Control Systems Project Engineer 1 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/35/4a195cb813825a6e3f2f0051ab520.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Thermo Systems | [View](https://www.openjobs-ai.com/jobs/control-systems-project-engineer-1-montgomery-al-127670000025600089) |
| Faculty Psychologist – Emory Brain Health – Atlanta, GA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/04/2ee2bbccf26b5aeac4507631ae1fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Headache Society | [View](https://www.openjobs-ai.com/jobs/faculty-psychologist-emory-brain-health-atlanta-ga-mount-royal-nj-127670000025600090) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/97/3fdfec10c6f726b11f273488ad009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Emergency Department | [View](https://www.openjobs-ai.com/jobs/registered-nurse-emergency-department-full-timepart-time-multiple-shifts-plainsboro-nj-127670000025600091) |
| Certified Nursing Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/00/f9097ae0140809b3de599f96f6248.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Skilled Nursing | [View](https://www.openjobs-ai.com/jobs/certified-nursing-assistant-skilled-nursing-full-time-nights-richmond-tx-127670000025600092) |
| Patient Liaison - Uveitis | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/49/4debbf2e7dc0606196145e523abc1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Retina Consultants of Texas | [View](https://www.openjobs-ai.com/jobs/patient-liaison-uveitis-bellaire-tx-127670000025600093) |
| Manager, Sr. Engineer, IT Financial Systems | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/fa/3715ee0df5ca5e72b0c4a00c64656.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Girl Scouts of the USA | [View](https://www.openjobs-ai.com/jobs/manager-sr-engineer-it-financial-systems-united-states-127670000025600094) |
| Summer 2026 Architectural Student Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/b5/b932e80b60dbfbc6afcfe4bcc76c6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Progressive Companies | [View](https://www.openjobs-ai.com/jobs/summer-2026-architectural-student-intern-durham-nc-127670000025600095) |
| First Assist Certified Surgical Tech - PRN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/16/eb7f343d8c9142856d7ab257ea40a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MUSC Health | [View](https://www.openjobs-ai.com/jobs/first-assist-certified-surgical-tech-prn-columbia-sc-127670000025600096) |
| Behavior Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/51/ebb4b74a4ec805d9288eb5884d341.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Total Spectrum, LLC | [View](https://www.openjobs-ai.com/jobs/behavior-technician-belleville-mi-127670000025600097) |
| CNA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/54/c5fcbd33788e4bd5730ff7d875169.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Certified Nursing Assistant | [View](https://www.openjobs-ai.com/jobs/cna-certified-nursing-assistant-pt-evenings-st-vincents-bismarck-nd-127670000025600098) |
| Material Handler - Forklift (2nd Shift) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/82/61408486241de1b06fb6d88c1add2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IAC Group | [View](https://www.openjobs-ai.com/jobs/material-handler-forklift-2nd-shift-arlington-tx-127670000025600099) |
| Senior/Staff AI Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/2b/e060f21f5099ea17f949773418c76.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Forterra | [View](https://www.openjobs-ai.com/jobs/seniorstaff-ai-engineer-east-palo-alto-ca-127670000025600100) |
| Medical Social Worker Hospice | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/e5/04c0d08b4d304d41b02b19eed8e62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OSF HealthCare | [View](https://www.openjobs-ai.com/jobs/medical-social-worker-hospice-galesburg-il-127670000025600101) |
| Personal Banker Associate I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/e9/4f94d9039dad145f1db303f521f4a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Huntsville, AL | [View](https://www.openjobs-ai.com/jobs/personal-banker-associate-i-huntsville-al-spanish-speaking-preferred-huntsville-al-127670000025600102) |
| Invasive Cardiovascular Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/35/1f4f484abe7647116dc9374ed11ca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hunterdon Health | [View](https://www.openjobs-ai.com/jobs/invasive-cardiovascular-technologist-flemington-nj-127670000025600103) |
| Registered Nurse (RN) - IV Team | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/91/59d977876480e94119a976fd1c393.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Catholic Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-iv-team-smithtown-ny-127670000025600104) |
| X-ray Tech | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/1e/259bfc254959459aebc14dc83a1e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Compass Surgical Partners | [View](https://www.openjobs-ai.com/jobs/x-ray-tech-center-in-127670000025600105) |
| IP Docketing Specialist - Remote Option Available | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/98/07c568ef6f4595adf810d20baad4e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Akerman LLP | [View](https://www.openjobs-ai.com/jobs/ip-docketing-specialist-remote-option-available-orlando-fl-127670000025600106) |
| Optometrist (OD) - Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/6f/b9effc53a71bbd110d74e3c304269.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MyEyeDr. | [View](https://www.openjobs-ai.com/jobs/optometrist-od-part-time-charlotte-nc-127670000025600107) |
| Software Engineering Manager, Checkout & Payments | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/40/3686170a3f2b9675ed9b22fc31500.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Squarespace | [View](https://www.openjobs-ai.com/jobs/software-engineering-manager-checkout-payments-new-york-ny-127670000025600108) |
| Entry Level Mechanical Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/7e/2b153d432799d6d05995c6314a74e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Salas O'Brien | [View](https://www.openjobs-ai.com/jobs/entry-level-mechanical-designer-raleigh-nc-127670000025600109) |
| Financial Services Sector Global Marketing Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/ac/8165ac4c77a3d55bc8a8d54c4d62a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> L.E.K. Consulting | [View](https://www.openjobs-ai.com/jobs/financial-services-sector-global-marketing-director-new-york-united-states-127670000025600110) |
| VP of Payroll Sales | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/da/33f398bbfc75f8cd6f8e3a9deb02f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Acrisure | [View](https://www.openjobs-ai.com/jobs/vp-of-payroll-sales-oklahoma-city-ok-127670000025600111) |
| Senior Consultant–Electronics Life Cycle Assessment | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/ca/a619b12559ad6a37ce02ee1e26624.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WSP | [View](https://www.openjobs-ai.com/jobs/senior-consultantelectronics-life-cycle-assessment-chicago-il-127670000025600112) |

<p align="center">
  <em>...and 595 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated January 25, 2026
</p>
