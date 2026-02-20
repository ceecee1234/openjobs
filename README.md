<p align="center">
  <img src="https://img.shields.io/badge/jobs-34+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-25+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 25+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 17 |
| Healthcare | 7 |
| Management | 5 |
| Sales | 3 |
| Engineering | 1 |
| Finance | 1 |
| Marketing | 0 |
| HR | 0 |
| Operations | 0 |

**Top Hiring Companies:** Allied Universal, CVS Health, 360 Behavioral Health, Brightview Senior Living, Teva Pharmaceuticals

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
│  │ Sitemap     │   │ (34+ jobs) │   │ (README + HTML)     │   │
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
- **And 25+ other companies**

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
  <em>Updated February 20, 2026 · Showing 34 of 34+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Security Officer College Campus Patrol Evenings | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-officer-college-campus-patrol-evenings-lancaster-ca-137454057160704036) |
| Security Officer - Residential Patrol | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-officer-residential-patrol-greenville-sc-137454057160704037) |
| Global Fire Safety Security Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/global-fire-safety-security-manager-indianapolis-in-137454057160704038) |
| Python Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/ce/ddcb41570c4d3715df4f7caa4d24e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BCforward | [View](https://www.openjobs-ai.com/jobs/python-developer-plano-tx-137454057160704039) |
| VP/National Sales Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/d5/d7e4a68bc70f27c98bb04f4f09845.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Western Equipment Finance | [View](https://www.openjobs-ai.com/jobs/vpnational-sales-manager-casa-grande-az-137454057160704040) |
| Lab Histotechnician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/c6/b8b957bff2a05b654e0f8fdfda355.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. Vincent Medical Center | [View](https://www.openjobs-ai.com/jobs/lab-histotechnician-st-vincent-medical-center-prn-toledo-oh-137454279458816000) |
| Employee Relations Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/03/450d0e26ed2579131dc0c48c8bbbe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> FL Department of Revenue | [View](https://www.openjobs-ai.com/jobs/employee-relations-consultant-tallahassee-fl-137454279458816002) |
| Product Manager, AI Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/54/c1ea5ff16f4d158914dbce9bb50d7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Moveworks | [View](https://www.openjobs-ai.com/jobs/product-manager-ai-operations-mountain-view-ca-137454279458816004) |
| Analyst Lead (Anaplan) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/cf/280244f222c5e315e06afd6a1d422.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Capital Group | [View](https://www.openjobs-ai.com/jobs/analyst-lead-anaplan-los-angeles-ca-137454279458816006) |
| Sports Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/74/1d03943f0f78e45551cfa3a631766.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> New England Return to Sport Center | [View](https://www.openjobs-ai.com/jobs/sports-physical-therapist-framingham-ma-137454669529088000) |
| Merchant Account Support Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/b1/21308e04070e24455dff9d7e238da.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fractal | [View](https://www.openjobs-ai.com/jobs/merchant-account-support-analyst-united-states-137454669529088001) |
| Electronics Assembler II (Contract to Hire) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2f/d9c9aaa25805ff4d31e2415ff9fcb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crane Aerospace & Electronics | [View](https://www.openjobs-ai.com/jobs/electronics-assembler-ii-contract-to-hire-lynnwood-wa-137454669529088002) |
| Associate Professor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/associate-professor-columbus-oh-137454669529088003) |
| Orthopaedic Institute | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/f8/cac30b742d64b4ec837083f80ce7b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Shoulder/Elbow Surgeon | [View](https://www.openjobs-ai.com/jobs/orthopaedic-institute-shoulderelbow-surgeon-erie-pa-erie-meadville-area-137454786969600000) |
| Exercise Physiologist Sr | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/43/4537f1d19c39f958a4e46f8c3491c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UVM Health | [View](https://www.openjobs-ai.com/jobs/exercise-physiologist-sr-south-burlington-vt-137454786969600001) |
| Salesperson | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f4/bf7e3f069a35415ef9405744545a9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Advance Auto Parts | [View](https://www.openjobs-ai.com/jobs/salesperson-paris-tn-137454786969600002) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/a6/1b1e66aa1eec0ef4e0c5160361bb1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Willis Knighton Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-louisiana-united-states-137454887632896000) |
| Automotive Editor/Motion Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/2c/433ce7438767e612360e5cfbb48ec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Motivated Marketing LLC | [View](https://www.openjobs-ai.com/jobs/automotive-editormotion-designer-north-charleston-sc-137454996684800000) |
| Shift Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/shift-supervisor-bloomfield-hills-mi-137454057160704019) |
| Security Officer - Manufacturer Building Patrol | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-officer-manufacturer-building-patrol-elkton-fl-137454057160704021) |
| Security Flex  Officer - Industrial Plant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-flex-officer-industrial-plant-lansing-mi-137454057160704022) |
| Security Shift Supervisor - Armed | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-shift-supervisor-armed-washington-united-states-137454057160704023) |
| Security Officer – High Tech Flex | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-officer-high-tech-flex-broomfield-co-137454057160704024) |
| Assistant Clinical Supervisor 2 PT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/13/f16e46dd5cce426f24ff119cbbc5b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 360 Behavioral Health | [View](https://www.openjobs-ai.com/jobs/assistant-clinical-supervisor-2-pt-riverside-ca-137454057160704025) |
| Community Sales Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/b4/6ba3f252215271eafbb6fec1f65fe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brightview Senior Living | [View](https://www.openjobs-ai.com/jobs/community-sales-director-east-brunswick-nj-137454057160704026) |
| Regulatory Affairs Associate I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/27/03255005facca7b78033ac6dd79bc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Teva Pharmaceuticals | [View](https://www.openjobs-ai.com/jobs/regulatory-affairs-associate-i-west-chester-pa-137454057160704027) |
| Pharmacy Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-technician-romney-wv-137454057160704028) |
| Pharmacy Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-technician-lady-lake-fl-137454057160704029) |
| Pharmacy Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-technician-plaistow-nh-137454057160704030) |
| Regional Vice President, Northeast | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/c1/c5c743568859910124fcc14e3aae5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Burns & Wilcox | [View](https://www.openjobs-ai.com/jobs/regional-vice-president-northeast-new-york-ny-137454057160704031) |
| Controller | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/f6/2321ee3c547898217eb951338d250.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LHH | [View](https://www.openjobs-ai.com/jobs/controller-orange-county-ca-137454057160704032) |
| HVAC Service Apprentice | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/55/19c84726e13d17029a8bbde4a30da.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lennox | [View](https://www.openjobs-ai.com/jobs/hvac-service-apprentice-greenville-sc-137454057160704033) |
| Clinical Analyst I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/9e/2d14606fb2fce33f9bf98975ab7be.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Memorial Healthcare | [View](https://www.openjobs-ai.com/jobs/clinical-analyst-i-owosso-mi-137454057160704034) |
| Security Officer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gatehouse | [View](https://www.openjobs-ai.com/jobs/security-officer-gatehouse-second-shift-fargo-nd-137454057160704035) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 20, 2026
</p>
