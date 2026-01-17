<p align="center">
  <img src="https://img.shields.io/badge/jobs-770+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-570+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 570+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 336 |
| Healthcare | 146 |
| Management | 113 |
| Engineering | 104 |
| Sales | 45 |
| Finance | 16 |
| Marketing | 4 |
| Operations | 4 |
| HR | 2 |

**Top Hiring Companies:** Epic, The Goodyear Tire & Rubber Company, Kroger Mountain View Foods, Inside Higher Ed, Koniag Government Services

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
│  │ Sitemap     │   │ (770+ jobs) │   │ (README + HTML)     │   │
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
- **And 570+ other companies**

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
  <em>Updated January 17, 2026 · Showing 200 of 770+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Staffing Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/3d/dca358200a02974d8e2b3debc943f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Open Arms Assisted Living, WI | [View](https://www.openjobs-ai.com/jobs/staffing-coordinator-racine-wi-125137324081152026) |
| Director of Nursing (DPCS) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/9d/827a852c376355a2a249a3760663b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Charter Healthcare | [View](https://www.openjobs-ai.com/jobs/director-of-nursing-dpcs-scottsdale-az-125137324081152027) |
| MTW Program Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/ca/1ce691c6383d2549a10eebe70b481.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Housing Authority of Joliet | [View](https://www.openjobs-ai.com/jobs/mtw-program-coordinator-joliet-il-125137324081152028) |
| Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/a6/95b0f2aa93800c23665df39ef932a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Princeton IT Services, Inc | [View](https://www.openjobs-ai.com/jobs/project-manager-united-states-125137324081152029) |
| Associate (Intern - Summer 2026), Management Consulting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/fe/7a8fdff8d62659b5503a54ddb7085.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alton Aviation Consultancy | [View](https://www.openjobs-ai.com/jobs/associate-intern-summer-2026-management-consulting-new-york-ny-125137324081152030) |
| Tax Director - National Tax Office (JD Required) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/37/7c5fc768db8e0accb17c715b8a562.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EisnerAmper | [View](https://www.openjobs-ai.com/jobs/tax-director-national-tax-office-jd-required-chicago-il-125137324081152031) |
| Cloud Engineer - Full Stack Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/d6/b18d9b1f827e291d98b82388071f7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Innovative Solutions | [View](https://www.openjobs-ai.com/jobs/cloud-engineer-full-stack-developer-washington-dc-125137324081152032) |
| Cloud Engineer - Full Stack Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/d6/b18d9b1f827e291d98b82388071f7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Innovative Solutions | [View](https://www.openjobs-ai.com/jobs/cloud-engineer-full-stack-developer-atlanta-ga-125137324081152033) |
| Local Delivery Driver (CDL A) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/c5/32f04de8a2b55e4e7cf1ee64114e1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Airgas | [View](https://www.openjobs-ai.com/jobs/local-delivery-driver-cdl-a-albany-ny-125137324081152034) |
| Lifeguard I & II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/87/49adf0fa9ad856bee573b80ba8668.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Loudoun County Government | [View](https://www.openjobs-ai.com/jobs/lifeguard-i-ii-loudoun-county-va-125137324081152035) |
| 1st & 2nd Grade Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/24/a0fedfa0f8f6b7637a20043359ec5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Archdiocese of St. Louis | [View](https://www.openjobs-ai.com/jobs/1st-2nd-grade-teacher-marthasville-mo-125137324081152036) |
| Litigation Paralegal - Stockton CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/85/53a894a7c8c59193e3e240784cc0a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sepulveda Sanchez Accident Lawyers | [View](https://www.openjobs-ai.com/jobs/litigation-paralegal-stockton-ca-stockton-ca-125137324081152037) |
| Certified Medical Assistant (MA)- Hematology Oncology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/35/95dddab495ffc7ed67a1714d3ca6e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Health First | [View](https://www.openjobs-ai.com/jobs/certified-medical-assistant-ma-hematology-oncology-melbourne-fl-125137324081152038) |
| IT Audit Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a5/3d0d510112d10ecca3470f200526b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PeopleCaddie | [View](https://www.openjobs-ai.com/jobs/it-audit-manager-oklahoma-city-ok-125137324081152039) |
| Hospice Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/14/5978719b28c0d309c436a867f39ca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Professional Healthcare Resources | [View](https://www.openjobs-ai.com/jobs/hospice-nurse-baltimore-md-125137324081152040) |
| Remote Commercial Collections LARGE BALANCE | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/81/0488627133920f09e0183d9849a92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Greenberg, Grant & Richards | [View](https://www.openjobs-ai.com/jobs/remote-commercial-collections-large-balance-buffalo-ny-125137324081152041) |
| HVAC Service Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/66/8690a405f9440c8b0c8bbdc9dcbfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lane Valente Industries | [View](https://www.openjobs-ai.com/jobs/hvac-service-technician-springfield-va-125137324081152042) |
| HVAC Service Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/66/8690a405f9440c8b0c8bbdc9dcbfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lane Valente Industries | [View](https://www.openjobs-ai.com/jobs/hvac-service-technician-little-rock-ar-125137324081152043) |
| Xray / CT Tech: FT Weekday/Weekend 2nd Shift (Sign-on Bonus) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/53/a292bed43e2bbbef075a546f1c157.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Riverview Health | [View](https://www.openjobs-ai.com/jobs/xray-ct-tech-ft-weekdayweekend-2nd-shift-sign-on-bonus-noblesville-in-125137324081152044) |
| HVAC Service Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/66/8690a405f9440c8b0c8bbdc9dcbfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lane Valente Industries | [View](https://www.openjobs-ai.com/jobs/hvac-service-technician-allentown-pa-125137324081152045) |
| HVAC Service Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/66/8690a405f9440c8b0c8bbdc9dcbfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lane Valente Industries | [View](https://www.openjobs-ai.com/jobs/hvac-service-technician-st-louis-mo-125137324081152046) |
| HVAC Service Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/66/8690a405f9440c8b0c8bbdc9dcbfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lane Valente Industries | [View](https://www.openjobs-ai.com/jobs/hvac-service-technician-akron-oh-125137324081152047) |
| Electrician - Nights | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/6e/55006ad61035777d44ba425eed721.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hartmann North America | [View](https://www.openjobs-ai.com/jobs/electrician-nights-rolla-mo-125137324081152048) |
| Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/ef/54287cbb4d1e38c10c476063fec87.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Integrated Power Services | [View](https://www.openjobs-ai.com/jobs/mechanic-beaumont-tx-125137324081152049) |
| Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/c6/1c8f6c4cab1b245bc9abce5bee7ba.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kimball Midwest | [View](https://www.openjobs-ai.com/jobs/sales-representative-moline-il-125137324081152050) |
| Software Validation Engineer, Actuators, Chassis Systems | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0b/90ccf85fb6d59c02cf47ec36866aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tesla | [View](https://www.openjobs-ai.com/jobs/software-validation-engineer-actuators-chassis-systems-palo-alto-ca-125137324081152051) |
| Strategic Account Executive MidAtlantic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/8b/935a9e44967691c05c3c651e56e45.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DocuWare | [View](https://www.openjobs-ai.com/jobs/strategic-account-executive-midatlantic-beacon-ny-125137324081152052) |
| RN - Cardiac Stepdown (Special Full Time) - 6028 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/3b/28b8bea0fffcbc2b4d84b32e45ed2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. Mary's Medical Center | [View](https://www.openjobs-ai.com/jobs/rn-cardiac-stepdown-special-full-time-6028-huntington-wv-125137324081152053) |
| RN - 2 South Med Surg | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/3b/28b8bea0fffcbc2b4d84b32e45ed2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> St. Mary's Medical Center | [View](https://www.openjobs-ai.com/jobs/rn-2-south-med-surg-huntington-wv-125137324081152054) |
| Cashier | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/cashier-roanoke-va-125137324081152055) |
| Cashier | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/cashier-cincinnati-oh-125137324081152056) |
| Cashier | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/cashier-sugar-hill-ga-125137324081152057) |
| Cashier | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/cashier-savannah-tn-125137324081152058) |
| Cashier | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/cashier-suffolk-va-125137324081152059) |
| Senior Deep Learning Performance Architect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/40/df7f83845146f0287ff6d2da77900.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NVIDIA | [View](https://www.openjobs-ai.com/jobs/senior-deep-learning-performance-architect-austin-tx-125137324081152060) |
| Field Service Technician (NETA 2) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/ec/5ffe6253e83c9b46e31eebc0afe29.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> POWERX | [View](https://www.openjobs-ai.com/jobs/field-service-technician-neta-2-tulsa-ok-125137324081152061) |
| Automotive Sales Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/70/99ca5bcf48c14ca202a90adae39fb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jenkins Kia of Gainesville | [View](https://www.openjobs-ai.com/jobs/automotive-sales-consultant-gainesville-fl-125137324081152062) |
| REGISTERED NURSE-Medicine RN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/39/7ced38162a5c7b7b3d33004e9a0d2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Yale New Haven Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-medicine-rn-bridgeport-ct-125137324081152063) |
| Solar Electrician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/2a/c6773a38bb49ee2f3791197009ea8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Green Power Energy | [View](https://www.openjobs-ai.com/jobs/solar-electrician-annandale-nj-125137324081152064) |
| Pool Weekend Warrior Dietary Aide | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/4b/0755525d3a83489d146ff1aaa2210.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Eaton County Health & Rehabilitation Services | [View](https://www.openjobs-ai.com/jobs/pool-weekend-warrior-dietary-aide-charlotte-mi-125137324081152065) |
| Director of Engineering, Trading Platforms | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/45/b2c33852abf3f9361a8ad0b4352ac.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NinjaTrader | [View](https://www.openjobs-ai.com/jobs/director-of-engineering-trading-platforms-chicago-il-125137324081152066) |
| CYBER Training Range Administration - Journeyman | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/83/97a16e4d2f6f17004d3918d096576.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> JBW Federal | [View](https://www.openjobs-ai.com/jobs/cyber-training-range-administration-journeyman-san-antonio-tx-125137324081152067) |
| Fire Suppression System Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/51/178a5e996a558ba6ce4dbc711840d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Afognak Native Corporation | [View](https://www.openjobs-ai.com/jobs/fire-suppression-system-mechanic-oklahoma-city-ok-125137324081152068) |
| Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/project-manager-butte-mt-125137324081152069) |
| Program Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/program-manager-washington-dc-125137324081152070) |
| Custodian, Second Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/custodian-second-shift-portsmouth-nh-125137324081152071) |
| Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/project-manager-charleston-sc-125137324081152072) |
| Cyber Governance, Risk and Compliance- SME II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/cyber-governance-risk-and-compliance-sme-ii-san-antonio-tx-125137324081152073) |
| RPA Lead Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/rpa-lead-engineer-washington-dc-125137324081152074) |
| Program Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/program-manager-washington-dc-125137324081152075) |
| Registered Nurse PT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/registered-nurse-pt-brunswick-ga-125137324081152076) |
| Cut To Length Maintenance Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e8/5dd3c64584b6be1b03b0664ab6e4b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SSAB | [View](https://www.openjobs-ai.com/jobs/cut-to-length-maintenance-technician-houston-tx-125137324081152077) |
| Tier 1 Network Administrator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/tier-1-network-administrator-washington-dc-125137324081152078) |
| Psychiatric Nurse Practitioner - Fee For Service | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/38/c2b06d5e5ab79e4cf55b90a963d14.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Thriveworks | [View](https://www.openjobs-ai.com/jobs/psychiatric-nurse-practitioner-fee-for-service-quincy-ma-125137324081152079) |
| Mechanical Project Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/2f/026fe4bf298dd7fda72dd0874ec92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IMEG | [View](https://www.openjobs-ai.com/jobs/mechanical-project-designer-rogers-ar-125137324081152080) |
| Part Time Licensed Talk Therapist - Fee For Service | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/38/c2b06d5e5ab79e4cf55b90a963d14.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Thriveworks | [View](https://www.openjobs-ai.com/jobs/part-time-licensed-talk-therapist-fee-for-service-cedar-rapids-ia-125137324081152081) |
| Policy Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b9/46b558d5b935bd6846213b8efcf78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Koniag Government Services | [View](https://www.openjobs-ai.com/jobs/policy-analyst-germantown-md-125137324081152082) |
| Bilingual Dealership Success Associate - Fort Lauderdale, FL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/5e/79fdfadfd1d6d1061641b1321fc9a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lendbuzz | [View](https://www.openjobs-ai.com/jobs/bilingual-dealership-success-associate-fort-lauderdale-fl-fort-lauderdale-fl-125137324081152083) |
| Occupational Therapist - Pediatric | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/f6/4ad0a29a33a64fc7bfe57e8ad6601.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sentara Health | [View](https://www.openjobs-ai.com/jobs/occupational-therapist-pediatric-chesapeake-va-125137324081152084) |
| Entry Level SUE Technician/Utility Locator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/4f/00c54a78ad8c6fe80bd97b9f8cbae.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> KCI | [View](https://www.openjobs-ai.com/jobs/entry-level-sue-technicianutility-locator-pittsburgh-pa-125137324081152085) |
| Business Relationship Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/65/3af70303b2a9768c709a19dce9e4c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Anchor Loans | [View](https://www.openjobs-ai.com/jobs/business-relationship-manager-united-states-125137324081152086) |
| Radiologic Technologist 1 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/c2/5c246c0d4e138c2391c7c4aef0105.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Nuvance Health | [View](https://www.openjobs-ai.com/jobs/radiologic-technologist-1-danbury-ct-125137324081152087) |
| Bakery/Deli Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/bakerydeli-clerk-owensboro-ky-125137324081152088) |
| Grocery Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/grocery-clerk-nashville-il-125137324081152089) |
| Online Grocery Pick-Up Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/online-grocery-pick-up-clerk-clarksville-in-125137324081152090) |
| Bakery/Deli Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/bakerydeli-clerk-friendswood-tx-125137324081152091) |
| Grocery Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/grocery-clerk-houston-tx-125137324081152092) |
| Store Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-member-macon-ga-125137324081152093) |
| Store Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-member-fort-smith-ar-125137324081152094) |
| Store Team Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-lead-concord-nc-125137324081152095) |
| Store Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-member-portland-tx-125137324081152096) |
| Store Team Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-lead-lexington-ky-125137324081152097) |
| Store Team Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-lead-oklahoma-city-ok-125137324081152098) |
| Store Team Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-lead-jeffersonville-in-125137324081152099) |
| Guest Services Attendant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/1c/fdf4b92a7d49cea6d5d03b0099627.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brigham and Women's Hospital | [View](https://www.openjobs-ai.com/jobs/guest-services-attendant-boston-ma-125137324081152100) |
| Store Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7c/942e6e8bfa28ff18635e2706aee20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Academy Sports + Outdoors | [View](https://www.openjobs-ai.com/jobs/store-team-member-madison-tn-125137324081152101) |
| VP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/7b/295d1979fdcd4fc0748a96cf30908.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Relationship Manager I | [View](https://www.openjobs-ai.com/jobs/vp-relationship-manager-i-cre-paramus-nj-125137324081152102) |
| 2nd shift Forklift Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/03/5cf85ae6d26455f311b065e68c4d6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DeltaPlus USA | [View](https://www.openjobs-ai.com/jobs/2nd-shift-forklift-operator-woodstock-ga-125137324081152103) |
| Commercial Lines Account Manager (Hybrid Opportunity) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/70/72610123def030dff282dbb675aff.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insurance Office of America | [View](https://www.openjobs-ai.com/jobs/commercial-lines-account-manager-hybrid-opportunity-las-vegas-nv-125137324081152104) |
| Registered Nurse RN Hospice | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/82/b249d925da32db22235973aa278ff.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amedisys | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-hospice-kennesaw-ga-125137324081152105) |
| General Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/84/1748914b6a8f4d2025f1b7493dd66.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Elephant Energy | [View](https://www.openjobs-ai.com/jobs/general-manager-boston-ma-125137324081152106) |
| Caregiver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/72/8cedc996bff4e6859f86cb0c27000.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Elite Home Health Care | [View](https://www.openjobs-ai.com/jobs/caregiver-new-york-ny-125137324081152108) |
| Nursing Instructor - Little Rock, AR (On-Site) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/cd/dbc1ec349b6b8b55fd0ab0a1e369b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaplan | [View](https://www.openjobs-ai.com/jobs/nursing-instructor-little-rock-ar-on-site-little-rock-ar-125137324081152109) |
| Accounting Advisory Team - Top Tier Management Consulting Firm | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/2f/8ad3838da37bac361aa82863a2f88.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WhiteCap Search | [View](https://www.openjobs-ai.com/jobs/accounting-advisory-team-top-tier-management-consulting-firm-new-york-ny-125137324081152110) |
| MRBC Legal Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/ab/1239044352325cdd1ffe1abedeece.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Law Offices of Ron Sholes, P.A. | [View](https://www.openjobs-ai.com/jobs/mrbc-legal-assistant-jacksonville-fl-125137324081152111) |
| Mental Health Program Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/5c/8ba55cd76125469c4ffbb0cb54ef0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stars Behavioral Health Group | [View](https://www.openjobs-ai.com/jobs/mental-health-program-director-los-angeles-ca-125137324081152112) |
| Java Developer with Copilot Studio(W2) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/44/8b51c36e08260a42aefa54aaf0cc8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Snowrelic Inc | [View](https://www.openjobs-ai.com/jobs/java-developer-with-copilot-studiow2-weehawken-nj-125137324081152113) |
| Senior Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/08/934dd716eb4f88083aa076fda3011.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Goldbelt Glacier Health Services | [View](https://www.openjobs-ai.com/jobs/senior-planner-united-states-125137324081152114) |
| Entry Level Outside Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/4c/4e7c150af95b0dd3e9ef16f4ffd05.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hibu | [View](https://www.openjobs-ai.com/jobs/entry-level-outside-sales-representative-west-hempstead-ny-125137324081152115) |
| Plant Operations Assistant, Full Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/ec/9b6e6b1754220b2583a0292266cc5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Maple Grove Senior Living | [View](https://www.openjobs-ai.com/jobs/plant-operations-assistant-full-time-shelbyville-ky-125137324081152116) |
| Advancement Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/9e/a8c1d2fa6856b6fc589b5970ed99e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cranbrook Educational Community | [View](https://www.openjobs-ai.com/jobs/advancement-coordinator-bloomfield-hills-mi-125137324081152117) |
| Assistant A&P Lead - 3 12s Weekends | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/8d/74c86c1b0c159970524c6f61b0f2a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> StandardAero | [View](https://www.openjobs-ai.com/jobs/assistant-ap-lead-3-12s-weekends-los-angeles-ca-125137324081152118) |
| PRN - Remote Utilization Review Work for a Neurosurgery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/3e/cf2f609ac5de12103b6a2eeea2637.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Medical Review Institute of America | [View](https://www.openjobs-ai.com/jobs/prn-remote-utilization-review-work-for-a-neurosurgery-dallas-tx-125137324081152119) |
| Machine Operator - Night Shift (4 Day Work Week!) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/3f/69c44e4a6ee7dceaa8285fce83c83.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Foundation Wellness | [View](https://www.openjobs-ai.com/jobs/machine-operator-night-shift-4-day-work-week-wadsworth-oh-125137324081152120) |
| Production Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/03/3eb5ced58797c902ab76fe34261ad.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Greene Tweed | [View](https://www.openjobs-ai.com/jobs/production-associate-kulpsville-pa-125137324081152121) |
| Packager I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/6d/0b87bf0e7630c8c4a2285066af0dd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hörmann North America | [View](https://www.openjobs-ai.com/jobs/packager-i-burgettstown-pa-125137324081152122) |
| Machine Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/6d/0b87bf0e7630c8c4a2285066af0dd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hörmann North America | [View](https://www.openjobs-ai.com/jobs/machine-operator-burgettstown-pa-125137324081152123) |
| Registered Nurse (RN) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/36/94c0a7a5e7fd7a23dd67ec08f4371.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Waukesha Memorial | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-waukesha-memorial-ortho-neuro-weekend-program-waukesha-wi-125137324081152124) |
| Mammography Technologist II - PRN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/c8/4f0155df53ee38613600d7970de26.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Health Images | [View](https://www.openjobs-ai.com/jobs/mammography-technologist-ii-prn-lakewood-co-125137324081152125) |
| Industrial Mechanic III - Duq | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/c5/6a3fc2cbae6e55c3e6acddf00cef1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Textile Company | [View](https://www.openjobs-ai.com/jobs/industrial-mechanic-iii-duq-duquesne-pa-125137324081152126) |
| Full-Time Occupational Therapy Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/32/a364e7cacb6671df26359ede4ba61.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Summit Care LLC | [View](https://www.openjobs-ai.com/jobs/full-time-occupational-therapy-assistant-olathe-ks-125137324081152127) |
| AR Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/28/b97c71a341b312e8d38c763ef4206.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NewGen Administrative Services | [View](https://www.openjobs-ai.com/jobs/ar-consultant-san-diego-metropolitan-area-125137324081152128) |
| Maintenance Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/d4/9850d145ec8e2aaf6e6a0bc08c269.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mechanical | [View](https://www.openjobs-ai.com/jobs/maintenance-specialist-mechanical-2nd-or-3rd-shift-frankfort-ky-125137324081152129) |
| Now Hiring: Part-Time, Weekend & PRN Caregivers – Build Your Career with Nurse Next Door | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/03/8c4f48a59b42c64505fe701bc9c15.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Nurse Next Door | [View](https://www.openjobs-ai.com/jobs/now-hiring-part-time-weekend-prn-caregivers-build-your-career-with-nurse-next-door-clayton-nc-125137324081152130) |
| Home Health Speech Therapist SLP Part Time Osceola County | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/3b/62a1b0d6aa6119b0ccdf0b2feef99.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aveanna Healthcare | [View](https://www.openjobs-ai.com/jobs/home-health-speech-therapist-slp-part-time-osceola-county-kissimmee-fl-125137324081152131) |
| Lab Technician II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/a3/3d46c60559ed120c6c58350900608.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Astera Labs | [View](https://www.openjobs-ai.com/jobs/lab-technician-ii-san-jose-ca-125137324081152132) |
| Entry-Level Behavior Analyst - RBT Training & Certification Paid | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/de/33a6388375436381aeb7a66ce46aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Comprehensive Behavior Supports | [View](https://www.openjobs-ai.com/jobs/entry-level-behavior-analyst-rbt-training-certification-paid-new-york-ny-125137324081152133) |
| Experienced Civil EIT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/9d/763bd266c87c7ec098f96a6b31fe2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kimley-Horn | [View](https://www.openjobs-ai.com/jobs/experienced-civil-eit-delray-beach-fl-125137324081152134) |
| Part Time Customer Sales Advisor - Shingle Springs, CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/part-time-customer-sales-advisor-shingle-springs-ca-shingle-springs-ca-125137324081152135) |
| Industrial Maintenance Technician - Lawton, OK | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/industrial-maintenance-technician-lawton-ok-lawton-ok-125137324081152136) |
| Roadside Technician Commercial Tires - Bremen, GA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/roadside-technician-commercial-tires-bremen-ga-bremen-ga-125137324081152137) |
| Entry Level Automotive Technician - Kahului, HI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/entry-level-automotive-technician-kahului-hi-kahului-hi-125137324081152138) |
| Entry Level Automotive Technician - Kahului, Hawaii | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/entry-level-automotive-technician-kahului-hawaii-kahului-hi-125137324081152139) |
| Automotive Technician - Vero Beach, FL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/automotive-technician-vero-beach-fl-vero-beach-fl-125137324081152140) |
| Truck Technician - Springdale, AR | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/truck-technician-springdale-ar-springdale-ar-125137324081152141) |
| Mid Level Automotive Technician - Edison, NJ | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/mid-level-automotive-technician-edison-nj-edison-nj-125137324081152142) |
| Mid Level Automotive Technician - Onalaska, WI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/mid-level-automotive-technician-onalaska-wi-onalaska-wi-125137324081152143) |
| Roadside Technician Commercial Tires (Training Provided) - East Walpole, MA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/roadside-technician-commercial-tires-training-provided-east-walpole-ma-east-walpole-ma-125137324081152144) |
| Mid Level Automotive Technician - Lake Worth, FL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/mid-level-automotive-technician-lake-worth-fl-lake-worth-fl-125137324081152145) |
| Roadside Technician Commercial Tires - Lafayette, LA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/roadside-technician-commercial-tires-lafayette-la-lafayette-la-125137324081152146) |
| Mid Level Automotive Technician -Eloy, AZ | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/mid-level-automotive-technician-eloy-az-eloy-az-125137324081152147) |
| Mid Level Automotive Technician (Oil & Tire) - Cuyahoga Falls, OH | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/mid-level-automotive-technician-oil-tire-cuyahoga-falls-oh-cuyahoga-falls-oh-125137324081152148) |
| Mid Level Automotive Technician - Ellicott City, MD | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/mid-level-automotive-technician-ellicott-city-md-ellicott-city-md-125137324081152149) |
| Assistant Service Manager - Parkersburg, WV | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/assistant-service-manager-parkersburg-wv-parkersburg-wv-125137324081152150) |
| Mid Level Automotive Technician - Denver, CO | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/mid-level-automotive-technician-denver-co-denver-co-125137324081152151) |
| Senior Narrative Designer (Writer) (Temporary) - Infinity Ward | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b3/2e27cdce84c80068ec4d75a0ebbe3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Infinity Ward | [View](https://www.openjobs-ai.com/jobs/senior-narrative-designer-writer-temporary-infinity-ward-los-angeles-ca-125137324081152152) |
| Deburr Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/04/e6051349f8bdf2dc84dc8b27f910b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ascentec Engineering, LLC | [View](https://www.openjobs-ai.com/jobs/deburr-technician-tualatin-or-125137324081152153) |
| EOC Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/24/d9040d53a20ebbef25d76e6e2e330.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ignite IT | [View](https://www.openjobs-ai.com/jobs/eoc-engineer-suitland-md-125137324081152154) |
| Orthopedic Surgery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/16/327ca95c72b68126911a7d1e58da4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Independent Medical Examiner (IME) | [View](https://www.openjobs-ai.com/jobs/orthopedic-surgery-independent-medical-examiner-ime-new-york-new-york-ny-125137324081152155) |
| Regional Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/e5/f3806a1ac6df5a6e736b67ae3a5f7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Justrite Safety Group | [View](https://www.openjobs-ai.com/jobs/regional-sales-representative-united-states-125137324081152156) |
| OKCarz | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/aa/b546108b29448420883746a290572.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Automotive Technician | [View](https://www.openjobs-ai.com/jobs/okcarz-automotive-technician-lakeland-lakeland-fl-125137324081152157) |
| Body Shop / Collision Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/5d/d43eb19b3ab0b6d04f2bbb3662ffb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cool Springs International, LLC | [View](https://www.openjobs-ai.com/jobs/body-shop-collision-technician-franklin-tn-125137324081152158) |
| Senior Technical Lead - Life Sciences, Veeva Vault RIM US | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/51/2a213af8ff080a12d14f434a1ba5f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> fme Life Sciences | [View](https://www.openjobs-ai.com/jobs/senior-technical-lead-life-sciences-veeva-vault-rim-us-united-states-125137324081152159) |
| Varsity Bowling Coach | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/dc/36374cdf563c1780c2100cd5f2ea7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Genesee Education Consultant Services (GECS) | [View](https://www.openjobs-ai.com/jobs/varsity-bowling-coach-burton-mi-125137324081152160) |
| Psychiatric Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/2d/e23f1a979f76f0911952d85962ffb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Harris Center for Mental Health and IDD | [View](https://www.openjobs-ai.com/jobs/psychiatric-technician-houston-tx-125137324081152161) |
| Product Manager, Knee Preservation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/ce/aae29bf0151e31e925010d41e583b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arthrex | [View](https://www.openjobs-ai.com/jobs/product-manager-knee-preservation-naples-fl-125137324081152162) |
| Associate Product Manager, Knee Preservation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/ce/aae29bf0151e31e925010d41e583b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arthrex | [View](https://www.openjobs-ai.com/jobs/associate-product-manager-knee-preservation-naples-fl-125137324081152163) |
| e-Discovery Paralegal | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/3b/4472e73626135cba110596219a677.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Construction Discovery Experts | [View](https://www.openjobs-ai.com/jobs/e-discovery-paralegal-dallas-fort-worth-metroplex-125137324081152164) |
| AC-Lite E2E Testing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/3a/8a0f0ca0ff82765b6c23e593a37f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EB Test Company | [View](https://www.openjobs-ai.com/jobs/ac-lite-e2e-testing-mountain-view-ca-125137324081152165) |
| PHLEBOTOMY TECHNICIAN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/36/15f2fbb427fbeb3cecacd22fdbe01.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cooper University Health Care | [View](https://www.openjobs-ai.com/jobs/phlebotomy-technician-camden-nj-125137324081152166) |
| Healthcare Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/49/1d8ed5188a265cb39a21f4a9ecfab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mercyhealth Wisconsin and Illinois | [View](https://www.openjobs-ai.com/jobs/healthcare-mechanic-janesville-wi-125137324081152167) |
| Senior Field Service Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/ea/ec9ce3246f49f8de0498775685730.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Schneider Electric | [View](https://www.openjobs-ai.com/jobs/senior-field-service-representative-denver-co-125137324081152168) |
| Heavy Equipment Mechanic - Sulphur, LA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/5c6290326cf5a0c19de65b4f9a115.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Altrad Sparrows Recruitment – Americas | [View](https://www.openjobs-ai.com/jobs/heavy-equipment-mechanic-sulphur-la-sulphur-la-125137324081152169) |
| Frontend Software Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/ab/9a57815c842f864c07cab39c7c2e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vinci4D.ai | [View](https://www.openjobs-ai.com/jobs/frontend-software-engineer-san-francisco-bay-area-125137324081152170) |
| Insurance Agency Owner-$20,000 agency opening BONUS! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/8a/de86b61455afd4437f515bbadc331.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AAA-The Auto Club Group | [View](https://www.openjobs-ai.com/jobs/insurance-agency-owner-20000-agency-opening-bonus-duluth-mn-125137324081152171) |
| Chief Operating Officer (COO) - Mortgage Lending | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/43/3aff9aa7a41803d97afd93d559c8c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AmeriSave Mortgage Corporation | [View](https://www.openjobs-ai.com/jobs/chief-operating-officer-coo-mortgage-lending-united-states-125137324081152172) |
| Architectural Project Manager - Hospitality / Hotels | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/cd/646fbf78797c8ae30df5698e0f617.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bancroft Staffing Partners (BSP) | [View](https://www.openjobs-ai.com/jobs/architectural-project-manager-hospitality-hotels-irvine-ca-125137324081152173) |
| Field Service Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/aa/f9567140cf2c2b9eb69f77c21d775.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Atlas Copco | [View](https://www.openjobs-ai.com/jobs/field-service-technician-columbia-sc-125137324081152174) |
| Orthodontist - Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/3c/9fe2ac6320a79774c26f70d890a1e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Specialty Dental Brands | [View](https://www.openjobs-ai.com/jobs/orthodontist-associate-millcreek-ut-125137324081152175) |
| Floating Outpatient Administrative Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/66/7f42a34d122fd1316de360909aeba.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> FLACRA | [View](https://www.openjobs-ai.com/jobs/floating-outpatient-administrative-assistant-rochester-new-york-metropolitan-area-125137324081152176) |
| Sales Account Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/3c/fc0a6272e35979d222235947b34fd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pace® Analytical Services | [View](https://www.openjobs-ai.com/jobs/sales-account-executive-allen-tx-125137324081152177) |
| Autism Care Team Member in Home Settings | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/de/33a6388375436381aeb7a66ce46aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Comprehensive Behavior Supports | [View](https://www.openjobs-ai.com/jobs/autism-care-team-member-in-home-settings-brooklyn-ny-125137324081152178) |
| Memory Care Resident Care Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/6d/576a7533c092e6620c1f0b380291b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Franciscan Ministries | [View](https://www.openjobs-ai.com/jobs/memory-care-resident-care-assistant-homer-glen-il-125137324081152179) |
| Federal Work Study | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/bc/2f275e81504887c7d01c05bcd8c14.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of South Carolina | [View](https://www.openjobs-ai.com/jobs/federal-work-study-chesterfield-county-sc-125137324081152180) |
| General Neurology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/2d/c1a8741deb09777a443c66cc763f5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NYU Langone Health | [View](https://www.openjobs-ai.com/jobs/general-neurology-manhattan-ny-125137324081152181) |
| Physical Therapy Assistant  Las Vegas, NM   Sign on Bonus | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/6e/6511b28e511eae9184f0c0cfe3f71.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Continuum Rehab Group | [View](https://www.openjobs-ai.com/jobs/physical-therapy-assistant-las-vegas-nm-sign-on-bonus-las-vegas-nm-125137324081152182) |
| RN OR DT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/91/ec225e7a9a1b4d182dbbcb14cb21f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Naples Comprehensive Health | [View](https://www.openjobs-ai.com/jobs/rn-or-dt-naples-fl-125137324081152183) |
| Technical Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/ef/54287cbb4d1e38c10c476063fec87.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Integrated Power Services | [View](https://www.openjobs-ai.com/jobs/technical-sales-representative-dallas-tx-125137324081152184) |
| Physical Therapist - Full Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/6e/61868fcf4f11698566f955148001d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cambridge Health Alliance | [View](https://www.openjobs-ai.com/jobs/physical-therapist-full-time-cambridge-ma-125137324081152185) |
| Senior Federal Electrical Engineering Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/cc/dcbc7ec60819cfb8bca1c20862b69.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HDR | [View](https://www.openjobs-ai.com/jobs/senior-federal-electrical-engineering-project-manager-walnut-creek-ca-125137324081152186) |
| Customer Service & Sales Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/ae/fd57355d5cddb61f0f99427fa407a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cathay Bank | [View](https://www.openjobs-ai.com/jobs/customer-service-sales-manager-brooklyn-ny-125137324081152187) |
| Registered Nurse, Med Telemetry Unit/Float, Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/fb/de81b7089fc9708df26cf1516e601.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UMass Memorial Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-med-telemetry-unitfloat-per-diem-clinton-ma-125137324081152188) |
| Senior Vice President, Director of Transaction Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/92/23884123060644bf5c6ac282df208.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AmeriHome Mortgage Company, LLC | [View](https://www.openjobs-ai.com/jobs/senior-vice-president-director-of-transaction-management-irvine-ca-125137324081152189) |
| Customer Service Representative - State Farm Agent Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/29/6642d139b1a83b74ad10b919847a7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State Farm Agent | [View](https://www.openjobs-ai.com/jobs/customer-service-representative-state-farm-agent-team-member-cedar-rapids-ia-125137324081152190) |
| Travel Registered Nurse Long Term Care | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/1b/4db9347e2907b68ce94537a0348b9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Coast Medical Service | [View](https://www.openjobs-ai.com/jobs/travel-registered-nurse-long-term-care-roseau-mn-125137324081152191) |
| Lead Operator (Shift Lead) - El Segundo, CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/0b/9a4445e09fd1c00a0094bd60281a6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jacobs | [View](https://www.openjobs-ai.com/jobs/lead-operator-shift-lead-el-segundo-ca-los-angeles-ca-125137324081152192) |
| Patient Care Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/b4/5818e687341e0104d4e71982f3544.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Smile Brands Inc. | [View](https://www.openjobs-ai.com/jobs/patient-care-coordinator-chicago-il-125137324081152193) |
| Womens Health Nurse Practitioner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/7e/92cfcb434147c1507024461781bf9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Christian Community Health Center | [View](https://www.openjobs-ai.com/jobs/womens-health-nurse-practitioner-chicago-il-125137324081152194) |
| Clinical Nurse V | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/88/8e77cd117a2e189461b4c4b14cb38.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Procedural Units | [View](https://www.openjobs-ai.com/jobs/clinical-nurse-v-procedural-units-operating-room-department-rocky-mount-nc-125137324081152195) |
| Maintenance Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/8b/f9488964c1723b02cfc66a7c5de5e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TCA Health Inc.- NFP | [View](https://www.openjobs-ai.com/jobs/maintenance-coordinator-chicago-il-125137324081152196) |
| Part-Time Art Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/87/27a0a9da2ebf432f790312cd5f138.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Specialized Education Services, Inc. | [View](https://www.openjobs-ai.com/jobs/part-time-art-teacher-belvidere-il-125137324081152197) |
| Vice President of Marketing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/82/ccadf952f7d4897e5c001bf258851.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UWorld | [View](https://www.openjobs-ai.com/jobs/vice-president-of-marketing-coppell-tx-125137324081152198) |
| Part Time Automotive Tire and Service Advisor - Raleigh, NC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/part-time-automotive-tire-and-service-advisor-raleigh-nc-raleigh-nc-125137324081152199) |
| Marketing Liaison - Skilled nursing and LTC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a9/e4acd7cce332f7aeff5066f0e3b2b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Morningside Ministries Senior Living Communities | [View](https://www.openjobs-ai.com/jobs/marketing-liaison-skilled-nursing-and-ltc-san-antonio-tx-125137324081152200) |
| Senior DevOps Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/58/afeedb246af5e95ee8f9543299292.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CACI International Inc | [View](https://www.openjobs-ai.com/jobs/senior-devops-engineer-melbourne-fl-125137324081152201) |
| Registered Dental Hygienist-Part Time-St Louis | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/b3/6b24f7566bd51405020f54df3f0d6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Enable Dental | [View](https://www.openjobs-ai.com/jobs/registered-dental-hygienist-part-time-st-louis-maryland-heights-mo-125137324081152202) |
| Respiratory Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/49/8abe7d8a31c2e6259e1db2d6b4bdf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Quipt Home Medical | [View](https://www.openjobs-ai.com/jobs/respiratory-therapist-stockbridge-ga-125137324081152203) |
| ENGINEER - WXIX | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/39/f317aa55059cf32216ebb7292fc81.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gray Media | [View](https://www.openjobs-ai.com/jobs/engineer-wxix-cincinnati-oh-125137324081152204) |
| Sales Tax Technology Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/34/baecfd5da0cd9d133c82c10c41a0d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crowe | [View](https://www.openjobs-ai.com/jobs/sales-tax-technology-manager-austin-tx-125137324081152205) |
| Sales Tax Technology Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/34/baecfd5da0cd9d133c82c10c41a0d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crowe | [View](https://www.openjobs-ai.com/jobs/sales-tax-technology-manager-boston-ma-125137324081152206) |
| Director, Real Estate Construction Project Delivery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/58/4922db22b2dbfb9a709883d45fdaa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fidelity Investments | [View](https://www.openjobs-ai.com/jobs/director-real-estate-construction-project-delivery-merrimack-nh-125137324081152207) |
| Retail Mortgage Loan Originator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/2d/ba2f7471000c09415c4451ee27173.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Truist | [View](https://www.openjobs-ai.com/jobs/retail-mortgage-loan-originator-myrtle-beach-sc-125137324081152208) |
| General Maintenance Technician - San Jose, CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dc/c1958eb71cab0bba21a99b4ec5c54.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Goodyear Tire & Rubber Company | [View](https://www.openjobs-ai.com/jobs/general-maintenance-technician-san-jose-ca-san-jose-ca-125137324081152209) |
| Client Solutions Center Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e0/12fd3632278c3fa39740100c078cc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Centier Bank | [View](https://www.openjobs-ai.com/jobs/client-solutions-center-specialist-merrillville-in-125137324081152210) |
| Associate Veterinarian - Kallison Ranch | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/be/c378982141e77ad445b62151116d9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CityVet | [View](https://www.openjobs-ai.com/jobs/associate-veterinarian-kallison-ranch-san-antonio-tx-125137324081152211) |
| System Architect Level II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/ff/b30f28d1a570e55f9278cc5b2579e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amyx, Inc. | [View](https://www.openjobs-ai.com/jobs/system-architect-level-ii-washington-dc-125137324081152212) |
| Online Grocery Pick-Up Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/online-grocery-pick-up-clerk-nashville-tn-125137324081152213) |
| STORE/NIGHT CLERK | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/storenight-clerk-cincinnati-oh-125137324081152214) |
| Cashier | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/cashier-louisville-ky-125137324081152215) |
| Porter (Kingsboro Men's MICA Shelter) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/3b/a797e9b6f2c34d53973e1bb007f72.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Salvation Army | [View](https://www.openjobs-ai.com/jobs/porter-kingsboro-mens-mica-shelter-brooklyn-ny-125137324081152216) |
| Manager Business Intelligence | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/ee/ec48d5986d37d239a12c1b6814b62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Liberty of Puerto Rico | [View](https://www.openjobs-ai.com/jobs/manager-business-intelligence-san-juan-carolina-area-125137793843200000) |
| LDAC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/e0/29b3d910b571e5f184c0b65d74192.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HARMON HOSPTAL | [View](https://www.openjobs-ai.com/jobs/ldac-las-vegas-nv-125137793843200001) |
| NC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/f4/68385d81ce225389ec0ae4f8765d9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Drake's Burlington | [View](https://www.openjobs-ai.com/jobs/nc-drakes-burlington-linecook-burlington-nc-125137793843200002) |
| Child & Adolescent Psychiatrist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/cf/79c3042c07ad796818e9bbaa1299f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Eating Recovery Center | [View](https://www.openjobs-ai.com/jobs/child-adolescent-psychiatrist-seattle-wa-125137793843200003) |
| Supply Chain Manager, Self-Driving & Infotainment Hardware | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0b/90ccf85fb6d59c02cf47ec36866aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tesla | [View](https://www.openjobs-ai.com/jobs/supply-chain-manager-self-driving-infotainment-hardware-palo-alto-ca-125137793843200004) |
| Protection and Control (P&C) Engineer – Transmission | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/0b/9a4445e09fd1c00a0094bd60281a6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jacobs | [View](https://www.openjobs-ai.com/jobs/protection-and-control-pc-engineer-transmission-los-angeles-ca-125137793843200005) |
| Principal Product Security Researcher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/de/1e9db895404e144f03055b11368d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Palo Alto Networks | [View](https://www.openjobs-ai.com/jobs/principal-product-security-researcher-santa-clara-ca-125137793843200006) |
| Hybrid BCBA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/f6/43d1c56c2bd3d918040eee63a3a8f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Always Shining ABA | [View](https://www.openjobs-ai.com/jobs/hybrid-bcba-elizabeth-nj-125138083250176000) |
| CRANE INSTALLER (Welding, Fabrication, Mechanic) 6A-2:30PM | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/15/b593b0d2b1cd34981dd147ecc360f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Custom Truck One Source | [View](https://www.openjobs-ai.com/jobs/crane-installer-welding-fabrication-mechanic-6a-230pm-kansas-city-mo-125138083250176001) |
| Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/fe/efae1331f28eb1dd86cca25b21ad1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SpeedPro | [View](https://www.openjobs-ai.com/jobs/project-manager-omaha-ne-125138083250176002) |

<p align="center">
  <em>...and 570 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated January 17, 2026
</p>
