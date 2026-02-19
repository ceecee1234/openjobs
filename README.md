<p align="center">
  <img src="https://img.shields.io/badge/jobs-53+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-42+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 42+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 24 |
| Healthcare | 10 |
| Engineering | 6 |
| Management | 5 |
| Sales | 4 |
| Finance | 3 |
| Marketing | 1 |
| HR | 0 |
| Operations | 0 |

**Top Hiring Companies:** Inside Higher Ed, Children's Healthcare of Atlanta, Addus HomeCare, The Faulkner Organization, DLB Associates

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
│  │ Sitemap     │   │ (53+ jobs) │   │ (README + HTML)     │   │
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
- **And 42+ other companies**

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
  <em>Updated February 19, 2026 · Showing 53 of 53+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Senior Project Manager - Construction Administration | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/18/ec43b557eb7bf5bc8fa1ef606b31b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DLB Associates | [View](https://www.openjobs-ai.com/jobs/senior-project-manager-construction-administration-united-states-137093338628096010) |
| Dietitian | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/d2/8f5e19e1aaafa180f7e8a30a37404.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Compass Healthcare | [View](https://www.openjobs-ai.com/jobs/dietitian-austin-tx-137093338628096011) |
| Senior Space Systems Engineer, Viasat Government | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/24/15f59ab9628708f5a8a09390e0057.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Viasat | [View](https://www.openjobs-ai.com/jobs/senior-space-systems-engineer-viasat-government-carlsbad-ca-137093338628096012) |
| Payroll Analyst - FPC or CPP certification required | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/76/a296b5bdcda93517a7e1c36b8dfda.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Children's Healthcare of Atlanta | [View](https://www.openjobs-ai.com/jobs/payroll-analyst-fpc-or-cpp-certification-required-brookhaven-ga-137093510594560000) |
| Physician - Pediatric Radiologist (Academic or Clinical Track) with Remote Option | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/76/a296b5bdcda93517a7e1c36b8dfda.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Children's Healthcare of Atlanta | [View](https://www.openjobs-ai.com/jobs/physician-pediatric-radiologist-academic-or-clinical-track-with-remote-option-georgia-137093510594560001) |
| Physician- Pediatric Hematologist, Inpatient Intensive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/76/a296b5bdcda93517a7e1c36b8dfda.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Children's Healthcare of Atlanta | [View](https://www.openjobs-ai.com/jobs/physician-pediatric-hematologist-inpatient-intensive-georgia-137093510594560002) |
| Business Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/40/b9a6d328f9f6698a4aac5594bd82d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Imploy | [View](https://www.openjobs-ai.com/jobs/business-analyst-mena-137093510594560003) |
| Hospice LPN On Call | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/4e/29ee5663f22c1c20ba0da3d839747.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Capital City Hospice | [View](https://www.openjobs-ai.com/jobs/hospice-lpn-on-call-columbus-oh-137093510594560004) |
| Assistant Product Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/40/b9a6d328f9f6698a4aac5594bd82d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Imploy | [View](https://www.openjobs-ai.com/jobs/assistant-product-manager-mena-137093510594560005) |
| Patient Service Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/52/6382af42fac5a00379356af44126e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Patient First | [View](https://www.openjobs-ai.com/jobs/patient-service-representative-aberdeen-md-137092944363520045) |
| Shipping/Receiving Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/8a/1927ed2581c9047e0acc64e96bd04.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Menasha Corporation | [View](https://www.openjobs-ai.com/jobs/shippingreceiving-lead-york-pa-137092944363520046) |
| QA/QC Administrative Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/89/b560ed6384a03d089e2df6679c976.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Phillips Foods | [View](https://www.openjobs-ai.com/jobs/qaqc-administrative-supervisor-halethorpe-md-137092944363520047) |
| Mobile Community Banker (Traveling Teller) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/d7/67f15f9695ca38b3acb31f2620442.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northfield Savings Bank VT | [View](https://www.openjobs-ai.com/jobs/mobile-community-banker-traveling-teller-vermont-united-states-137092944363520048) |
| Full-Time CRNA (Certified Registered Nurse Anesthetist) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/80/ec5fa29b807cc809431a193519bce.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Our Lady of Lourdes Hospital | [View](https://www.openjobs-ai.com/jobs/full-time-crna-certified-registered-nurse-anesthetist-our-lady-of-lourdes-hospital-camden-nj-camden-nj-137092944363520049) |
| Home Care Aide | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/4e/67b9271758edace29205a88209e73.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Addus HomeCare | [View](https://www.openjobs-ai.com/jobs/home-care-aide-flora-il-137092944363520050) |
| Home Care Aide | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/4e/67b9271758edace29205a88209e73.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Addus HomeCare | [View](https://www.openjobs-ai.com/jobs/home-care-aide-oil-city-pa-137092944363520051) |
| Automotive Technician/Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/32/00933714cbb12927816f4e1921180.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Faulkner Organization | [View](https://www.openjobs-ai.com/jobs/automotive-technicianmechanic-bethlehem-pa-137092944363520052) |
| Automotive Technician/Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/32/00933714cbb12927816f4e1921180.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Faulkner Organization | [View](https://www.openjobs-ai.com/jobs/automotive-technicianmechanic-willow-grove-pa-137092944363520053) |
| Financial Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/89/30f1b458c53c23037d5586436cf33.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Marathon TS | [View](https://www.openjobs-ai.com/jobs/financial-analyst-scott-afb-il-137092944363520054) |
| Accounting Manager/Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/04/e341b3160d4a365ebfa980e7fc91a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Robert Half | [View](https://www.openjobs-ai.com/jobs/accounting-managersupervisor-honolulu-hi-137092944363520055) |
| Assistant Professor Pathology and Laboratory Medicine | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/assistant-professor-pathology-and-laboratory-medicine-philadelphia-pa-137092944363520056) |
| Assistant Professor of Dramatic Writing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/assistant-professor-of-dramatic-writing-binghamton-ny-137092944363520057) |
| Early Childhood Studies Instructor (Part-Time Faculty Pool) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/early-childhood-studies-instructor-part-time-faculty-pool-fremont-ca-137092944363520058) |
| Faculty Physician / Clinician Educator (Chatham Hospital) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/faculty-physician-clinician-educator-chatham-hospital-chapel-hill-nc-137092944363520059) |
| Assistant Professor, Academic Clinician Track | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/assistant-professor-academic-clinician-track-philadelphia-pa-137092944363520060) |
| CMCR Supervisor (6811U) University Health Services 83316 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/cmcr-supervisor-6811u-university-health-services-83316-berkeley-ca-137092944363520061) |
| HVAC Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/12/7a0ef588d8ea94399ab7e1e49537e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pearce Services | [View](https://www.openjobs-ai.com/jobs/hvac-technician-el-cajon-ca-137092944363520062) |
| Risk Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/80/20f3cd27af58eca9c48426bfb1c4f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CCB Risk Execution UAT Lead | [View](https://www.openjobs-ai.com/jobs/risk-management-ccb-risk-execution-uat-lead-senior-associate-plano-tx-137092944363520063) |
| Account Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/db/69075feb9bb8bb433f46cc16cb68c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lev | [View](https://www.openjobs-ai.com/jobs/account-executive-new-york-city-metropolitan-area-137092944363520064) |
| Operation Program Engineer (A Group OPM 02 ) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/16/94e032d50e9dcad2812a0a0740d53.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 鴻海精密工業股份有限公司 | [View](https://www.openjobs-ai.com/jobs/operation-program-engineer-a-group-opm-02--houston-tx-137092944363520065) |
| Dental Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/51/c4b665a9944096cc73fd9fbbb4f64.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DOCS Health | [View](https://www.openjobs-ai.com/jobs/dental-assistant-virginia-beach-va-137093141495808000) |
| Client Intake Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/9d/3c6dd62d828e25a7ff0fa0e45e460.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Price Benowitz LLP | [View](https://www.openjobs-ai.com/jobs/client-intake-specialist-latin-america-137093141495808001) |
| Manufacturing Product Engineer (LFAB) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/50/69b3be86508e4521f0c915131b921.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Texas Instruments | [View](https://www.openjobs-ai.com/jobs/manufacturing-product-engineer-lfab-lehi-ut-137093141495808002) |
| Find Your Work Fam | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/41/9d5bef98582880d36ad5d9fc07c91.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AlphaGraphics on University | [View](https://www.openjobs-ai.com/jobs/find-your-work-fam-bedford-nh-137093141495808003) |
| Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/8b/3c9b0ba65a23c392394aa1a30cd2a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Evolve Psychiatry | [View](https://www.openjobs-ai.com/jobs/therapist-albany-ny-137093141495808004) |
| Home Infusion Nurse (RN) - Lakeland/Plant City | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/f2/5e69ad1ffabd544ee5c903fbd8ea7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Prosper Infusion | [View](https://www.openjobs-ai.com/jobs/home-infusion-nurse-rn-lakelandplant-city-florida-united-states-137093141495808005) |
| Box Truck Driver & Furniture Installer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/c7/26541093faf116dcd77023148b763.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CORT | [View](https://www.openjobs-ai.com/jobs/box-truck-driver-furniture-installer-hayward-ca-137093141495808006) |
| Construction Superintendent - Mechanical | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/bb/b833f19257d0c0fab30f3487cf626.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ramboll | [View](https://www.openjobs-ai.com/jobs/construction-superintendent-mechanical-syracuse-ny-137093141495808007) |
| Brand Ambassador | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b6/44e6eff7e391631c3c93ceda8e03d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sandpiper Productions | [View](https://www.openjobs-ai.com/jobs/brand-ambassador-hogansville-ga-137093141495808008) |
| Traveling Electronic Security Systems Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/a5/7ca8b06c35fe4102be4d35a4ec56f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Evergreen Fire and Security | [View](https://www.openjobs-ai.com/jobs/traveling-electronic-security-systems-technician-tallahassee-fl-137093141495808009) |
| Tax Manager - Business Tax Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/67/d8a24535e51ec7afc13d757361537.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RubinBrown LLP | [View](https://www.openjobs-ai.com/jobs/tax-manager-business-tax-services-kansas-city-ks-137093141495808010) |
| AWS Lead Cloud Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/5c/5f966753b4584e83462a60d3e62cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LightFeather | [View](https://www.openjobs-ai.com/jobs/aws-lead-cloud-engineer-washington-dc-137093141495808011) |
| Licensed CAM | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/7d/1e0401b3dbf81737c2765cad97974.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Premier Association Management, LLC | [View](https://www.openjobs-ai.com/jobs/licensed-cam-debary-fl-137093141495808013) |
| Service Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/c5/3f1108b0b66d0ac128a15ccb244db.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crain Automotive Holdings, LLC | [View](https://www.openjobs-ai.com/jobs/service-advisor-springdale-ar-137093141495808014) |
| Generator Service Technician, Generator Services Team | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/17/f09b91594e1b16f374b34593d895d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amazon Web Services (AWS) | [View](https://www.openjobs-ai.com/jobs/generator-service-technician-generator-services-team-plain-city-oh-137093141495808015) |
| Heavy Equipment Shop Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/66/9a9ad10541e405f9637b5e15f5fc9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stowers Machinery Corporation | [View](https://www.openjobs-ai.com/jobs/heavy-equipment-shop-technician-knoxville-tn-137093141495808016) |
| Exciting Opportunity: Join Us as a Remote Sales Professional in the Cutting-Edge AI Field! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/f8/cbc151df6f50146e06eea25194e07.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> JGRobo Marketing, Inc. | [View](https://www.openjobs-ai.com/jobs/exciting-opportunity-join-us-as-a-remote-sales-professional-in-the-cutting-edge-ai-field-united-states-137093338628096000) |
| Licensed Outpatient Therapist (Remote, Flexible Hours) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/a4/0d49cbc7b89808a1a387341b284d3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ConsciousAbraxas | [View](https://www.openjobs-ai.com/jobs/licensed-outpatient-therapist-remote-flexible-hours-minnesota-united-states-137093338628096001) |
| Senior Software Engineer, Integrations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4c/019d0f53d465bd016098362c89cb2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Paragon | [View](https://www.openjobs-ai.com/jobs/senior-software-engineer-integrations-los-angeles-metropolitan-area-137093338628096002) |
| Electrical Engineer III | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/18/ec43b557eb7bf5bc8fa1ef606b31b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DLB Associates | [View](https://www.openjobs-ai.com/jobs/electrical-engineer-iii-united-states-137093338628096003) |
| Sales Operations Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/2b/75f73d1c35f4b290d89895aa64717.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brown & Brown | [View](https://www.openjobs-ai.com/jobs/sales-operations-coordinator-united-states-137093338628096004) |
| Maintenance Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/f6/5458aaa5a5e4dc4e2f93d55279c0e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Virginia Department of Veterans Services | [View](https://www.openjobs-ai.com/jobs/maintenance-technician-suffolk-va-137093338628096006) |
| Principal, Business Development [Embedded Partnerships] | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/cd/a99d74dd9165c27c8e811d8ea60a8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Remote | [View](https://www.openjobs-ai.com/jobs/principal-business-development-embedded-partnerships-united-states-137093338628096008) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 19, 2026
</p>
