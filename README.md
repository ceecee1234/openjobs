<p align="center">
  <img src="https://img.shields.io/badge/jobs-76+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-72+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 72+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 36 |
| Healthcare | 13 |
| Engineering | 11 |
| Management | 8 |
| Sales | 6 |
| Finance | 1 |
| HR | 1 |
| Marketing | 0 |
| Operations | 0 |

**Top Hiring Companies:** QUANTEAM (RAINBOW PARTNERS Group), Northwestern Mutual, Luxury Bath Technologies Corporate, Ford Motor Company, Parker Hannifin

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
│  │ Sitemap     │   │ (76+ jobs) │   │ (README + HTML)     │   │
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
- **And 72+ other companies**

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
  <em>Updated February 07, 2026 · Showing 76 of 76+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Eddy Heritage House Clinical Hiring Week | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/25/0023a075e5f50d0df443dc3ff8206.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. Peter's Health Partners | [View](https://www.openjobs-ai.com/jobs/eddy-heritage-house-clinical-hiring-week-troy-ny-132744097038336015) |
| CNA / Day Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/db/7c868964797362743bc0a01cec847.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> National HealthCare Corporation (NHC) | [View](https://www.openjobs-ai.com/jobs/cna-day-shift-nashville-tn-132744097038336016) |
| Customer Success Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/8a/6fcc3bb7fb0cb45bb8d748a309bbe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crayon | [View](https://www.openjobs-ai.com/jobs/customer-success-manager-boston-ma-132744097038336017) |
| Member of Technical Staff - Copilot AI Companion Engineering Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/f5/32a3fc4f1ea403f37070f59a7a53a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Microsoft | [View](https://www.openjobs-ai.com/jobs/member-of-technical-staff-copilot-ai-companion-engineering-manager-mountain-view-ca-132744097038336018) |
| Registered Nurse Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/80/635ff895a1c7ceb247d5b04a7fce6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Friendly Senior Living | [View](https://www.openjobs-ai.com/jobs/registered-nurse-supervisor-forest-home-ny-132744097038336019) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/63/bf5c4caf1b0f406d3f14864c3b95d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brown University Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-providence-ri-132744097038336020) |
| Vascular Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/0f/ea3112f6a58ec5216ab24a1f3e551.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Presbyterian Healthcare Services | [View](https://www.openjobs-ai.com/jobs/vascular-technologist-clovis-nm-132744097038336021) |
| Battery Materials Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/c4/a541b22d7d407dfd9f52412aec208.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> GDI | [View](https://www.openjobs-ai.com/jobs/battery-materials-technician-rochester-ny-132744097038336022) |
| Outside Sales Representative - Wilmington Region $5000.00 Signing-Performance Bonus | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/99/f6d69d1de21a05343e7f35e449459.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Omni Fiber | [View](https://www.openjobs-ai.com/jobs/outside-sales-representative-wilmington-region-500000-signing-performance-bonus-wilmington-oh-132744097038336023) |
| Assistant Teacher Full Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/6a/d4a274d315cbd0c5f3113ca988e63.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goddard School | [View](https://www.openjobs-ai.com/jobs/assistant-teacher-full-time-malvern-pa-132744097038336024) |
| Certified Medication Aide (CMA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/37/0ecaaa0bd563239fc20067938cf8e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Americare Senior Living | [View](https://www.openjobs-ai.com/jobs/certified-medication-aide-cma-columbia-mo-132744331919360000) |
| Principal Strategy and Operations Manager, US Marketing and Customer Growth | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/principal-strategy-and-operations-manager-us-marketing-and-customer-growth-mountain-view-ca-132744331919360001) |
| Research Software in the Loop (SIL) Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/f2/3060d2d9a5f97157f1aab641a2941.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ford Motor Company | [View](https://www.openjobs-ai.com/jobs/research-software-in-the-loop-sil-supervisor-dearborn-mi-132743585333248053) |
| Sr. Supplier Quality Engineer - Aerospace | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f8/5bdbf3173c126db15806827ada278.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Parker Hannifin | [View](https://www.openjobs-ai.com/jobs/sr-supplier-quality-engineer-aerospace-camarillo-ca-132743585333248054) |
| System Administrator 1 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/53/229d545fe1864566b7b556ad9bfcf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Orion Consortium, LLC | [View](https://www.openjobs-ai.com/jobs/system-administrator-1-fort-meade-md-132743585333248055) |
| Physician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/82/7e319be36f74e88957363e1b3cb92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ObGyn Vice Chair of Clinical Operations | [View](https://www.openjobs-ai.com/jobs/physician-obgyn-vice-chair-of-clinical-operations-chicago-24150-chicago-il-132743585333248056) |
| SAF-IS Regional Program Specialist - RESERVE | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/79/87cb1eafedd8fa85b55b1be8687fe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Red Cross | [View](https://www.openjobs-ai.com/jobs/saf-is-regional-program-specialist-reserve-texas-united-states-132743585333248057) |
| Campaign Growth Leader | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/01/b1104c708ccf71edb82881e054009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Guidehouse | [View](https://www.openjobs-ai.com/jobs/campaign-growth-leader-atlanta-ga-132743585333248058) |
| Retail Sales Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/1b/06eabf65e5cf375d391cbe91ef6aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Mattress | [View](https://www.openjobs-ai.com/jobs/retail-sales-associate-lapeer-mi-132743585333248059) |
| Sales Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/6b/c69645f3d43c538e747d5b4456188.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dartronics, Inc. | [View](https://www.openjobs-ai.com/jobs/sales-engineer-philadelphia-pa-132743585333248060) |
| Co-Op, Materials Process Engineer, Fall 2026 (July - December) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/0a/bc0ddf33fb1dc768e420a50fc94e5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alloy Enterprises Inc | [View](https://www.openjobs-ai.com/jobs/co-op-materials-process-engineer-fall-2026-july-december-burlington-ma-132743585333248061) |
| Production Associate - (Organic) $19.70 p/hr (11AM Start) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/39/3886e2f56446a7d27008df4faf9b9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Flowers Foods & Subsidiaries | [View](https://www.openjobs-ai.com/jobs/production-associate-organic-1970-phr-11am-start-henderson-nv-132743585333248062) |
| Pension Risk Transfer Senior Contract Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/d5/da2123303a66fabd8603155d994e1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Reinsurance Group of America, Incorporated | [View](https://www.openjobs-ai.com/jobs/pension-risk-transfer-senior-contract-analyst-new-york-ny-132743585333248063) |
| Executive Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/95/6ad0e6995089d6903c76d3db0d27a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cabrillo Economic Development Corporation | [View](https://www.openjobs-ai.com/jobs/executive-assistant-ventura-ca-132743585333248064) |
| Casual Snubber Tech Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/52/51a81246eae224cb736d542c1e6d3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Element Materials Technology | [View](https://www.openjobs-ai.com/jobs/casual-snubber-tech-specialist-huntsville-al-132743585333248065) |
| College Financial Representative, Internship Program | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/5e/28e5c91a1fd30daf4bfcc8fb1a73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northwestern Mutual | [View](https://www.openjobs-ai.com/jobs/college-financial-representative-internship-program-rockland-ma-132743585333248066) |
| Sr. Software Engineer, Distributed Systems, Autobidder Platform | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0b/90ccf85fb6d59c02cf47ec36866aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tesla | [View](https://www.openjobs-ai.com/jobs/sr-software-engineer-distributed-systems-autobidder-platform-austin-tx-132743585333248067) |
| Senior Software Developer (AI/ML integration) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/6b/81075e345644672e05e273fc817ae.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. George Tanaq Corporation | [View](https://www.openjobs-ai.com/jobs/senior-software-developer-aiml-integration-salem-or-132743585333248069) |
| Financial Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/5e/28e5c91a1fd30daf4bfcc8fb1a73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northwestern Mutual | [View](https://www.openjobs-ai.com/jobs/financial-advisor-center-valley-pa-132743585333248070) |
| Sr Mobile Inspector, Manheim, King of Prussia, PA ($1,500 sign on bonus) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/ab/7f1a8565540900a18e2f1937139a1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cox Automotive Inc. | [View](https://www.openjobs-ai.com/jobs/sr-mobile-inspector-manheim-king-of-prussia-pa-1500-sign-on-bonus-philadelphia-pa-132743585333248072) |
| Mergers & Acquisitions Product Technology Diligence Senior Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/39/954f26fc843dc265a62e9669e09d3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Deloitte | [View](https://www.openjobs-ai.com/jobs/mergers-acquisitions-product-technology-diligence-senior-consultant-los-angeles-ca-132743585333248073) |
| Associate Director, Statistical Programming | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/55/238be997dd4ff94763c4255202a8a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kardigan | [View](https://www.openjobs-ai.com/jobs/associate-director-statistical-programming-princeton-nj-132743585333248074) |
| Python Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/ab/ef4b5553d0d261a95df26ae7c8495.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intellias | [View](https://www.openjobs-ai.com/jobs/python-developer-minneapolis-mn-132743585333248075) |
| Manager of Cybersecurity | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/02/add543003b6c6d1aab1b0d8ac1780.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hyundai Motor Company | [View](https://www.openjobs-ai.com/jobs/manager-of-cybersecurity-montgomery-al-132743585333248076) |
| Pharmacy Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-technician-sacramento-ca-132743585333248077) |
| Sr Admin Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/2e/f13115ef4a42088f078061090f86a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Imagine | [View](https://www.openjobs-ai.com/jobs/sr-admin-assistant-shakopee-mn-132743585333248078) |
| Patient Account Rep | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/20/7c13cae40fabb573ee23cda3432a1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Community Health Network | [View](https://www.openjobs-ai.com/jobs/patient-account-rep-indianapolis-in-132743585333248079) |
| Med Surg Nursing Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/5a/c99e193873cd941885f9c9f0bb78e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Full Time Nights | [View](https://www.openjobs-ai.com/jobs/med-surg-nursing-assistant-full-time-nights-gaylord-mi-gaylord-mi-132743585333248080) |
| Business Development Director – CPG | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/10/2646095106f3b65ee482cdf50bf91.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mintel | [View](https://www.openjobs-ai.com/jobs/business-development-director-cpg-chicago-il-132743585333248081) |
| Water & Wastewater Engineer Intern (E.I.) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/d5/2ab8443faf58c98e1c680f11a1d9e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> JEO Consulting Group, Inc. | [View](https://www.openjobs-ai.com/jobs/water-wastewater-engineer-intern-ei-south-sioux-city-ne-132743585333248082) |
| Beekeeper - Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/de/9c96d4c661bb5bebc1353c3a26907.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Best Bees Company | [View](https://www.openjobs-ai.com/jobs/beekeeper-part-time-seattle-wa-132743585333248083) |
| Senior Sales Consultant - New Business | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/13/4ba620c5a8930a7e7e15dd34dceb2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> KONE | [View](https://www.openjobs-ai.com/jobs/senior-sales-consultant-new-business-trumbull-ct-132743585333248084) |
| Audiology Technician (Princeton, NJ) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/b6/963cc2621770393a36185e2ba9c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Starkey Hearing | [View](https://www.openjobs-ai.com/jobs/audiology-technician-princeton-nj-princeton-nj-132743585333248085) |
| Physical Therapist $5K Sign On Bonus | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/5b/d59a4d84b71fec4d3eb9329ab4a35.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SSM Health Physical Therapy | [View](https://www.openjobs-ai.com/jobs/physical-therapist-5k-sign-on-bonus-lake-st-louis-mo-132743585333248086) |
| Project Manager, Planning Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/0a/a3747aafcc7b2e8a03648e089fe70.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gordian | [View](https://www.openjobs-ai.com/jobs/project-manager-planning-services-illinois-united-states-132743585333248087) |
| Hematologist Oncologist - Astera Cancer Care | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/68/57cb939bfe9deca59099949c1a906.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OneOncology | [View](https://www.openjobs-ai.com/jobs/hematologist-oncologist-astera-cancer-care-toms-river-nj-132743836991488000) |
| Acrylic Bath Installer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/5b/125ddc6dd757a058930119179b9d5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Luxury Bath Technologies Corporate | [View](https://www.openjobs-ai.com/jobs/acrylic-bath-installer-port-huron-mi-132743836991488001) |
| Acrylic Bath Installer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/5b/125ddc6dd757a058930119179b9d5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Luxury Bath Technologies Corporate | [View](https://www.openjobs-ai.com/jobs/acrylic-bath-installer-warren-mi-132743836991488002) |
| Diagnostic Radiology Technologist I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/e5/04c0d08b4d304d41b02b19eed8e62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OSF HealthCare | [View](https://www.openjobs-ai.com/jobs/diagnostic-radiology-technologist-i-bloomington-il-132743941849088000) |
| Direct Support Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/92/6c04331cb3e8fab91729f08408afb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Apace (formerly Region V Services) | [View](https://www.openjobs-ai.com/jobs/direct-support-professional-wahoo-ne-132743941849088001) |
| Mental Health Clinician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e0/a7d71c26e1c20307cee69d23f6f1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hyacinth Foundation | [View](https://www.openjobs-ai.com/jobs/mental-health-clinician-paterson-nj-132743941849088002) |
| PT RECREATION (BUILDING ATTENDANT I) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/d4/cfd678c8ebe081063f97fbf0cfa3e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of Lompoc | [View](https://www.openjobs-ai.com/jobs/pt-recreation-building-attendant-i-lompoc-ca-132743941849088003) |
| Sales Engineer (Remote – Based in China) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/e5/f7d8863b7e0aa291e2232f18a01a6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Augmentus Robotics | [View](https://www.openjobs-ai.com/jobs/sales-engineer-remote-based-in-china-united-states-132743941849088004) |
| Consultant(e) Développement Trading C++ H/F – New York | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/57/d1dd573efa0e20cfec9a5fec29800.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> QUANTEAM (RAINBOW PARTNERS Group) | [View](https://www.openjobs-ai.com/jobs/consultante-dveloppement-trading-c-hf-new-york-new-york-united-states-132743941849088005) |
| Développeur(euse) Commando Front Office – C# ou Python H/F – New York | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/57/d1dd573efa0e20cfec9a5fec29800.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> QUANTEAM (RAINBOW PARTNERS Group) | [View](https://www.openjobs-ai.com/jobs/dveloppeureuse-commando-front-office-c-ou-python-hf-new-york-new-york-united-states-132743941849088006) |
| Consultant(e) Support d’Application Post-Trade H/F – Chicago | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/57/d1dd573efa0e20cfec9a5fec29800.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> QUANTEAM (RAINBOW PARTNERS Group) | [View](https://www.openjobs-ai.com/jobs/consultante-support-dapplication-post-trade-hf-chicago-chicago-il-132743941849088007) |
| Account Executive Job Overview | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/92/5069246c18dd2c2dbb3ecccc1af5a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cyber Infrastructure (CIS) | [View](https://www.openjobs-ai.com/jobs/account-executive-job-overview-chicago-il-132743941849088008) |
| Pediatric Hospitalist Moonlighting - Nemours Children's Health, Jefferson Einstein Phila Hospital | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/fa/90e8802a42c54d46178d429667254.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Nemours Children's Health | [View](https://www.openjobs-ai.com/jobs/pediatric-hospitalist-moonlighting-nemours-childrens-health-jefferson-einstein-phila-hospital-philadelphia-pa-132743941849088009) |
| Receptionist - State Farm Agent Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/29/6642d139b1a83b74ad10b919847a7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State Farm Agent | [View](https://www.openjobs-ai.com/jobs/receptionist-state-farm-agent-team-member-holland-mi-132743941849088010) |
| MCDHH Interpreter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/63/89ee2dfe79292464d496d24f43d35.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of Missouri | [View](https://www.openjobs-ai.com/jobs/mcdhh-interpreter-jefferson-city-mo-132743941849088011) |
| Inventory Specialist Part Time 30 Hours | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/c5/569b7d005a151dc4aefff6913d29c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Copart | [View](https://www.openjobs-ai.com/jobs/inventory-specialist-part-time-30-hours-sacramento-ca-132743941849088012) |
| SITE COACH | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/6c/56d3dd4717de662c18fe5935000c4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Goodwill Southeast Georgia | [View](https://www.openjobs-ai.com/jobs/site-coach-kingsland-ga-132744097038336000) |
| Senior Home & Kitchen Editor, Forbes Vetted | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/e6/dcb68102e9985fc1b5f65fcebec66.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Forbes | [View](https://www.openjobs-ai.com/jobs/senior-home-kitchen-editor-forbes-vetted-united-states-132744097038336001) |
| Technical Operations Manager, Operations Workflow Automation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/eb/337396eecd5c727ea89003c0df2d3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Commure | [View](https://www.openjobs-ai.com/jobs/technical-operations-manager-operations-workflow-automation-mountain-view-ca-132744097038336002) |
| AVP Customer Contact Center - GM Protections | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/3c/d01e876770e46c840189445da0b0f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> GM Financial | [View](https://www.openjobs-ai.com/jobs/avp-customer-contact-center-gm-protections-irving-tx-132744097038336003) |
| Advanced Surgical Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/7d/32f031c872a5c0b96e737cfaaf132.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ozarks, AR | [View](https://www.openjobs-ai.com/jobs/advanced-surgical-consultant-ozarks-ar-johnson-johnson-medtech-heart-recovery-danvers-ma-132744097038336004) |
| Senior Engineer - Directed Energy Team & Capture Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/36/bfa0fb2716ff876f5e33854cc9648.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ARA | [View](https://www.openjobs-ai.com/jobs/senior-engineer-directed-energy-team-capture-lead-albuquerque-nm-132744097038336005) |
| General Labor, Bakery-Packing L7 - 1st Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/89/dd64b59ef1fefa259a77e4689ff00.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aspire Bakeries | [View](https://www.openjobs-ai.com/jobs/general-labor-bakery-packing-l7-1st-shift-swedesboro-nj-132744097038336006) |
| RN Interventional Radiology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/56/25193c22e01bbce91e2f54446ed78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Corewell Health | [View](https://www.openjobs-ai.com/jobs/rn-interventional-radiology-grand-rapids-mi-132744097038336007) |
| RN Value Analysis | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/2e/5197978ef00556a89426389272b53.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tucson Medical Center | [View](https://www.openjobs-ai.com/jobs/rn-value-analysis-tucson-az-132744097038336008) |
| Floater Pharmacist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/96/ad41d00f7cbd066d7ef38e2520bbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cardinal Health | [View](https://www.openjobs-ai.com/jobs/floater-pharmacist-nashville-tn-132744097038336009) |
| GTM CIO US Public Sector (PS) Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1c/d6e549ab60b728497f73aeeccc9ba.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ServiceNow | [View](https://www.openjobs-ai.com/jobs/gtm-cio-us-public-sector-ps-director-santa-clara-ca-132744097038336010) |
| Senior Account Executive – US (Enterprise \| AI / SaaS) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a7/2ca3faf88d325a2cb8a76fd150f79.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Whale | [View](https://www.openjobs-ai.com/jobs/senior-account-executive-us-enterprise-ai-saas-united-states-132744097038336011) |
| Chess Instructor \| Winter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/eb/24ac8ae25fa0dc40a67f37e5621c9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Chess Wizards, Inc | [View](https://www.openjobs-ai.com/jobs/chess-instructor-winter-winnetka-il-132744097038336012) |
| LICENSED PRACTICAL NURSE BEHAVIORAL HEALTH SERVICES UNIT 12-A PART-TIME DAY SHIFT 20732 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/25/812a47e3e24d5d5673d72398a595a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bergen New Bridge Medical Center | [View](https://www.openjobs-ai.com/jobs/licensed-practical-nurse-behavioral-health-services-unit-12-a-part-time-day-shift-20732-paramus-nj-132744097038336013) |
| SunTrax Facilities Maintenance Manager - Auburndale, FL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/0b/9a4445e09fd1c00a0094bd60281a6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jacobs | [View](https://www.openjobs-ai.com/jobs/suntrax-facilities-maintenance-manager-auburndale-fl-tampa-fl-132744097038336014) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 07, 2026
</p>
