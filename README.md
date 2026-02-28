<p align="center">
  <img src="https://img.shields.io/badge/jobs-583+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-347+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 347+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 332 |
| Healthcare | 96 |
| Management | 73 |
| Engineering | 43 |
| Sales | 22 |
| Finance | 8 |
| Operations | 7 |
| Marketing | 1 |
| HR | 1 |

**Top Hiring Companies:** Intuit, CPA, ORAU, Heritage Manor Care, Sutter Health

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
│  │ Sitemap     │   │ (583+ jobs) │   │ (README + HTML)     │   │
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
- **And 347+ other companies**

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
  <em>Updated February 28, 2026 · Showing 200 of 583+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Physical Therapist (PRN/Weekends) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/59/312df8b75a8a92f103fe2881c54b3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tulsa Rehabilitation Hospital | [View](https://www.openjobs-ai.com/jobs/physical-therapist-prnweekends-tulsa-ok-140353441103872349) |
| Registered Behavior Technician RBT/BT - Part-Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/01/a654b025ba14b3a006818b27c814d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ABA Centers of America | [View](https://www.openjobs-ai.com/jobs/registered-behavior-technician-rbtbt-part-time-milford-ma-140353441103872350) |
| Exoplanets - NASA High-Resolution Speckle Imaging Program | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/exoplanets-nasa-high-resolution-speckle-imaging-program-santa-clara-county-ca-140353441103872351) |
| Respiratory Therapist (RRT/CRT) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/c0/1c5ba9c7d1bf651c582c2f430da30.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Geisinger | [View](https://www.openjobs-ai.com/jobs/respiratory-therapist-rrtcrt-wilkes-barre-pa-140353441103872352) |
| Occupational Therapy Assistant - Rehabilitation Center of Sandalwood | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/63/e810709b6511371bef851ec16930f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Flagship Therapy | [View](https://www.openjobs-ai.com/jobs/occupational-therapy-assistant-rehabilitation-center-of-sandalwood-wheat-ridge-co-140353441103872353) |
| Coronal and Solar Wind Models and the Data Used to Drive and Validate Them | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/coronal-and-solar-wind-models-and-the-data-used-to-drive-and-validate-them-greenbelt-md-140353441103872354) |
| Manager, Construction Manager - Baldwin Park, CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/5d/0aac9b091e8a1c001ab78acce07fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente | [View](https://www.openjobs-ai.com/jobs/manager-construction-manager-baldwin-park-ca-baldwin-park-ca-140353441103872355) |
| Auto Body Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/71/d82f576ca424b8d14d1d32feb910a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gerber Collision & Glass | [View](https://www.openjobs-ai.com/jobs/auto-body-technician-charlotte-nc-140353441103872356) |
| NASA Goddard Space Flight Center Cold Atom Interferometry and Optical Clocks4/14 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/nasa-goddard-space-flight-center-cold-atom-interferometry-and-optical-clocks414-greenbelt-md-140353441103872357) |
| Solar System Exploration: Dynamics of Planetary Atmospheres | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/solar-system-exploration-dynamics-of-planetary-atmospheres-greenbelt-md-140353441103872358) |
| Development of infrared detectors and focal plane arrays for space instruments | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/development-of-infrared-detectors-and-focal-plane-arrays-for-space-instruments-pasadena-ca-140353441103872359) |
| Outside Sales Representative - $1,000 Sign On Bonus | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/67/f61b598046a22da7b83a8ba8c0710.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hawx Smart Pest Control | [View](https://www.openjobs-ai.com/jobs/outside-sales-representative-1000-sign-on-bonus-waltham-ma-140353441103872360) |
| Registered Behavior Technician RBT/BT - Full-Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/0e/48530a8c12931a93ce74907463e85.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ABA Centers of Virginia | [View](https://www.openjobs-ai.com/jobs/registered-behavior-technician-rbtbt-full-time-fairfax-va-140353441103872361) |
| California fault processes constrained by InSAR andGPS observations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/california-fault-processes-constrained-by-insar-andgps-observations-pasadena-ca-140353441103872362) |
| Substitute Nurses for Magnet Schools and Special Education Outplacement Programs | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/39/d8d14024f2ae5c8dc2e07362eba1d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LEARN | [View](https://www.openjobs-ai.com/jobs/substitute-nurses-for-magnet-schools-and-special-education-outplacement-programs-old-lyme-ct-140353441103872363) |
| Analytical and Computational Research Tools for Advanced Materials and Structures | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/analytical-and-computational-research-tools-for-advanced-materials-and-structures-hampton-va-140353441103872364) |
| Science Preparations for the Habitable Worlds Observatory | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/science-preparations-for-the-habitable-worlds-observatory-greenbelt-md-140353441103872365) |
| Senior Director, Corporate Development | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/2c/cda10db94c2b5d51beed10484c025.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HP | [View](https://www.openjobs-ai.com/jobs/senior-director-corporate-development-palo-alto-ca-140353441103872366) |
| Studying the Reionization Epoch with Superconducting On-Chip Spectroscopy | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/studying-the-reionization-epoch-with-superconducting-on-chip-spectroscopy-pasadena-ca-140353441103872368) |
| CHHA and CNA Hospice Aide 1,000 Sign-On-Bonus | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/82/b249d925da32db22235973aa278ff.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amedisys | [View](https://www.openjobs-ai.com/jobs/chha-and-cna-hospice-aide-1000-sign-on-bonus-toms-river-nj-140353441103872369) |
| Senior Clinician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/d2/19d24aa8596ad5f326eff7200c0b5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Old Colony YMCA | [View](https://www.openjobs-ai.com/jobs/senior-clinician-dartmouth-ma-140353441103872370) |
| Development of Next-Generation Thermopile Arrays for Space Applications | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/development-of-next-generation-thermopile-arrays-for-space-applications-pasadena-ca-140353441103872371) |
| Understanding Methane Point Source Emissions | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/understanding-methane-point-source-emissions-pasadena-ca-140353441103872372) |
| RN Labor & Delivery NN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/91/ec225e7a9a1b4d182dbbcb14cb21f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Naples Comprehensive Health | [View](https://www.openjobs-ai.com/jobs/rn-labor-delivery-nn-naples-fl-140353441103872373) |
| Student Nursing Technician - Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/4f/0fbb3dbc31deff0ba43e919553a52.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hartford HealthCare | [View](https://www.openjobs-ai.com/jobs/student-nursing-technician-per-diem-meriden-ct-140353441103872374) |
| Inside Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/1c/36a6bacfc9f72d44b9f65d32d401b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Goosehead Insurance | [View](https://www.openjobs-ai.com/jobs/inside-sales-representative-dallas-fort-worth-metroplex-140353441103872375) |
| Heliophysics Science: Global Magnetospheric Simulation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/heliophysics-science-global-magnetospheric-simulation-greenbelt-md-140353441103872377) |
| New challenges in Stratospheric Sciences: Asian Pollution and Extreme Wildfire Smoke | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/new-challenges-in-stratospheric-sciences-asian-pollution-and-extreme-wildfire-smoke-hampton-va-140353441103872378) |
| Imaging | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/47/4ab77c8faeffcb7d556cd467b8da9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Echo/Vascular Ultrasound Technician | [View](https://www.openjobs-ai.com/jobs/imaging-echovascular-ultrasound-technician-prn-sidney-oh-140353441103872379) |
| Resident Customer Support Engineer (Onsite - Sterling, VA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/96/36db519d560813084383cd0376b73.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> VAST Data | [View](https://www.openjobs-ai.com/jobs/resident-customer-support-engineer-onsite-sterling-va-sterling-va-140353441103872380) |
| AI Security Researcher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/84/726f75e078a60934a41380e88a076.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wiz | [View](https://www.openjobs-ai.com/jobs/ai-security-researcher-united-states-140353441103872381) |
| Part Time Teller (20 Hours), Eastridge Branch, Bilingual Preferred: Vietnamese | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/f83c90ef9f50c06d88cf660f9eca9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Citi | [View](https://www.openjobs-ai.com/jobs/part-time-teller-20-hours-eastridge-branch-bilingual-preferred-vietnamese-san-jose-ca-140353441103872382) |
| Seasonal Tax Associate - Work from Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-associate-work-from-home-duncannon-pa-140353441103872383) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-remote-union-city-ga-140353441103872384) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-remote-minneapolis-mn-140353441103872385) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-work-from-home-darlington-sc-140353441103872386) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-millington-tn-140353441103872387) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-remote-sandston-va-140353441103872388) |
| Customer Experience Specialist, Gallery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0b/90ccf85fb6d59c02cf47ec36866aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tesla | [View](https://www.openjobs-ai.com/jobs/customer-experience-specialist-gallery-strongsville-oh-140353441103872389) |
| Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/78/aa7a2b8c230519343fbda4a70aae7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PRN | [View](https://www.openjobs-ai.com/jobs/physical-therapist-prn-bowling-green-kentucky-bowling-green-ky-140353441103872390) |
| Seasonal Tax Associate - Local | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-associate-local-sioux-city-ia-140353441103872391) |
| Seasonal Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA or EA | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-expert-cpa-or-ea-work-from-home-saukville-wi-140353441103872392) |
| Customer Success Manager USA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/7b/5c7b5738e648a062473d9eccf60f4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Qovery | [View](https://www.openjobs-ai.com/jobs/customer-success-manager-usa-new-york-united-states-140353441103872393) |
| Full Time Evening Custodian | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/55/ec15b8ccccd49958c01b2c078a7ea.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Central Maintenance & Service Co. Inc. | [View](https://www.openjobs-ai.com/jobs/full-time-evening-custodian-crafton-pa-140353441103872394) |
| Senior Customer Success Manager, TOLA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/bc/e262aee6fd79a66ac4776e2ad0a72.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Abnormal AI | [View](https://www.openjobs-ai.com/jobs/senior-customer-success-manager-tola-united-states-140353441103872395) |
| Director of Philanthropy | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/director-of-philanthropy-santa-clara-ca-140353441103872396) |
| Nurse Practitioner- Cardiac Surgery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/nurse-practitioner-cardiac-surgery-oakland-ca-140353441103872397) |
| Inside Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/b8/71911c0d1dcd532421b296f16231f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OpenSpace | [View](https://www.openjobs-ai.com/jobs/inside-sales-representative-united-states-140353441103872398) |
| Outside Sales Professional - Oklahoma City | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/22/d55b6d82133db12c8696d83f6072b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tom James Company | [View](https://www.openjobs-ai.com/jobs/outside-sales-professional-oklahoma-city-oklahoma-city-ok-140353441103872399) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-penitas-tx-140353441103872400) |
| Manufacturing Production Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/55/19c84726e13d17029a8bbde4a30da.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lennox | [View](https://www.openjobs-ai.com/jobs/manufacturing-production-operator-tifton-ga-140353441103872401) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-mulvane-ks-140353441103872402) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-berwick-me-140353441103872403) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-leicester-nc-140353441103872404) |
| Seasonal Credentialed Tax Expert - Bilingual Spanish | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-tax-expert-bilingual-spanish-bradenton-fl-140353441103872405) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-omaha-ne-140353441103872406) |
| ROLL STOCK TRUCKER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/0d/064794720f5072cb960e1f3b93f6f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Packaging Corporation of America | [View](https://www.openjobs-ai.com/jobs/roll-stock-trucker-woodway-tx-140353441103872407) |
| Office Coordinator - On Call | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/96/4a82ac27a4b3e7206f2555290c89a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Comprehensive Healthcare | [View](https://www.openjobs-ai.com/jobs/office-coordinator-on-call-yakima-wa-140353441103872408) |
| RN Quality Assurance Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/eb/d1a15e7e900e93ce4597fe4c04bab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RHA Health Services, LLC | [View](https://www.openjobs-ai.com/jobs/rn-quality-assurance-specialist-raleigh-nc-140353441103872409) |
| Seasonal Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA or EA | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-expert-cpa-or-ea-work-from-home-mohegan-lake-ny-140353441103872410) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-petal-ms-140353441103872411) |
| Seasonal Business Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-expert-bradenton-fl-140353441103872412) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enrolled Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enrolled-agent-or-practicing-attorney-seasonal-remote-swedesboro-nj-140353441103872413) |
| Seasonal Bilingual Credentialed Tax Professional - Remote | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-remote-reno-nv-140353441103872414) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-seasonal-remote-tallahassee-fl-140353441103872415) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-piscataway-nj-140353441103872416) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enroll Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enroll-agent-or-practicing-attorney-seasonal-remote-poplar-grove-il-140353441103872417) |
| Work From Home Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/work-from-home-bilingual-tax-professional-cpa-seasonal-bernalillo-nm-140353441103872418) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-remote-chicago-il-140353441103872419) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-valatie-ny-140353441103872420) |
| Product Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/2a/1c4509cc54eff98e7883e42a6f9c1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> iRhythm Technologies, Inc. | [View](https://www.openjobs-ai.com/jobs/product-designer-united-states-140353441103872421) |
| Seasonal Operations Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/9b/0e3a8ab4792bdfd18d89d72cafafa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Go McPherson | [View](https://www.openjobs-ai.com/jobs/seasonal-operations-specialist-lindsborg-ks-140353441103872422) |
| Systems Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9b/8584a8f73e22cb5ab5f5c51204979.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MANTECH | [View](https://www.openjobs-ai.com/jobs/systems-analyst-crane-in-140353441103872423) |
| Specialist - Power Electronics (SW&S) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/78/975dcd26b82d618105a45bed30a57.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> India Nippon Electricals Limited- INEL | [View](https://www.openjobs-ai.com/jobs/specialist-power-electronics-sws-centre-county-pa-140353441103872424) |
| BMW Apprentice Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/4a/c047544ed1c020a4f49647c42e322.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bill Jacobs BMW | [View](https://www.openjobs-ai.com/jobs/bmw-apprentice-technician-naperville-il-140353441103872425) |
| Market Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/1e/070e05913e6f63a88e52baea91dc6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Thrivent | [View](https://www.openjobs-ai.com/jobs/market-director-nashville-tn-140353441103872426) |
| Senior Forensic Engineer - Mechanical | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/02/1bf4248f08b40ee66533f34e1e923.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> YA Group | [View](https://www.openjobs-ai.com/jobs/senior-forensic-engineer-mechanical-united-states-140353441103872427) |
| Account Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/65/716ee735be9ff49f38cad97007586.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> InfuCare Rx® | [View](https://www.openjobs-ai.com/jobs/account-manager-florida-united-states-140353441103872428) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-plain-city-oh-140353441103872429) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-richmond-va-140353441103872430) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-ridgeland-ms-140353441103872431) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-edwardsburg-mi-140353441103872432) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-remote-blissfield-mi-140353441103872433) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-remote-port-st-lucie-fl-140353441103872434) |
| Construction Inspector | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1b/9196acc395f41b152c44f6029ee51.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Laland Baptiste | [View](https://www.openjobs-ai.com/jobs/construction-inspector-rochester-ny-140353441103872435) |
| Sr. Simulation Engineer, Material Flow | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fd/3923880df8acc6083287622f18e3f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rivian | [View](https://www.openjobs-ai.com/jobs/sr-simulation-engineer-material-flow-normal-il-140353441103872436) |
| Project Environmental Scientist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/a6/a745e9d37d6f37032db5eb6095491.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Olsson | [View](https://www.openjobs-ai.com/jobs/project-environmental-scientist-oklahoma-city-ok-140353441103872437) |
| Coordinator Review Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/5d/0aac9b091e8a1c001ab78acce07fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente | [View](https://www.openjobs-ai.com/jobs/coordinator-review-services-renton-wa-140353441103872438) |
| Bank Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/a3/ad57f792cb59504fb407cf3c8680a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BMO U.S. | [View](https://www.openjobs-ai.com/jobs/bank-manager-albuquerque-nm-140353441103872439) |
| Tax Associate - Local | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/tax-associate-local-sioux-city-ia-140353441103872440) |
| Seasonal Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA or EA | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-expert-cpa-or-ea-work-from-home-zebulon-nc-140353441103872441) |
| Seasonal Tax Associate - Work from Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-associate-work-from-home-sand-springs-ok-140353441103872442) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-wilmington-il-140353441103872443) |
| Seasonal Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA or EA | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-expert-cpa-or-ea-work-from-home-el-cajon-ca-140353441103872444) |
| Seasonal Bilingual Credentialed Tax Professional - Remote | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-remote-pensacola-fl-140353441103872445) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-greenville-sc-140353441103872446) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-oklahoma-city-ok-140353441103872447) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-remote-birmingham-al-140353441103872448) |
| Technical Account Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/8c/9aa11aa0e8abcac8c3d08ecb32894.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Chemtrade | [View](https://www.openjobs-ai.com/jobs/technical-account-manager-united-states-140353441103872449) |
| Software Engineer, Data Migration & Code Generation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/d1/6bb63833747b7c4b9adce2e66bbcf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MongoDB | [View](https://www.openjobs-ai.com/jobs/software-engineer-data-migration-code-generation-new-mexico-united-states-140353441103872450) |
| Budtender | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/13/741160fcb97ab2952ec8c5d0155a3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DACUT | [View](https://www.openjobs-ai.com/jobs/budtender-detroit-mi-140353441103872451) |
| General Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/94/672943fefbfc46776024917dd842c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Community Choice Financial Family of Brands | [View](https://www.openjobs-ai.com/jobs/general-manager-chattanooga-tn-140353441103872452) |
| EY-Parthenon | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/12/9e72d68b2dfc2b50a5c724ae47efe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Strategy and Execution | [View](https://www.openjobs-ai.com/jobs/ey-parthenon-strategy-and-execution-growth-platforms-ai-ml-engineering-director-san-francisco-ca-140353441103872453) |
| Registered Nurse II, PICC Float | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-ii-picc-float-castro-valley-ca-140353441103872454) |
| Computed Tomography (CT) Technologist III | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/computed-tomography-ct-technologist-iii-novato-ca-140353441103872455) |
| Electronics Lab Assembly/Solder Technician- onsite Huntsville, AL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/46/ea72c850081dc761067a3e3961613.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Raytheon | [View](https://www.openjobs-ai.com/jobs/electronics-lab-assemblysolder-technician-onsite-huntsville-al-huntsville-al-140353441103872456) |
| Physical Design Engineer (Silicon Engineering) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/f0/ff813c3676d81a04a616ba555af0c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SpaceX | [View](https://www.openjobs-ai.com/jobs/physical-design-engineer-silicon-engineering-sunnyvale-ca-140353441103872457) |
| Seasonal Business Tax Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-associate-sachse-tx-140353441103872458) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-miami-fl-140353441103872459) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-remote-houston-tx-140353441103872460) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-saunderstown-ri-140353441103872461) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enrolled Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enrolled-agent-or-practicing-attorney-seasonal-remote-ligonier-pa-140353441103872462) |
| Seasonal Bilingual Credentialed Tax Professional - Remote | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-remote-birmingham-al-140353441103872463) |
| Civil Engineering Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/9d/763bd266c87c7ec098f96a6b31fe2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kimley-Horn | [View](https://www.openjobs-ai.com/jobs/civil-engineering-intern-austin-tx-140353441103872464) |
| Pharmacy Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-technician-sacramento-ca-140353441103872465) |
| Plant Safety Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/35/6457bb1b6931f902ac163857cfb31.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Leprino | [View](https://www.openjobs-ai.com/jobs/plant-safety-manager-greeley-co-140353441103872466) |
| Receptionist - PCA Lake Otis Urgent Care | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/4c/07a1f8338998f008db58b60c65a3d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Orthopedic Physicians Alaska | [View](https://www.openjobs-ai.com/jobs/receptionist-pca-lake-otis-urgent-care-anchorage-ak-140353441103872467) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-riverton-nj-140353441103872468) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enrolled Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enrolled-agent-or-practicing-attorney-seasonal-remote-orland-park-il-140353441103872469) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-st-paul-mn-140353441103872470) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-work-from-home-las-cruces-nm-140353441103872471) |
| Seasonal Bilingual Credentialed Tax Professional - Remote | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-remote-harvard-il-140353441103872472) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-remote-springfield-mo-140353441103872473) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-georgetown-de-140353441103872474) |
| Work From Home Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/work-from-home-bilingual-tax-professional-cpa-seasonal-greenville-sc-140353441103872475) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-work-from-home-rehoboth-ma-140353441103872476) |
| Seasonal Credentialed Tax Expert - Bilingual Spanish | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-tax-expert-bilingual-spanish-cedar-rapids-ia-140353441103872477) |
| Work From Home Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/work-from-home-bilingual-tax-professional-cpa-seasonal-charleston-sc-140353441103872478) |
| Seasonal Credentialed Tax Expert - Bilingual Spanish | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-tax-expert-bilingual-spanish-thermal-ca-140353441103872479) |
| Inline Trainer (2nd Shift) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/a3/a1b3d7c7dc76a2db9c6761c1d856f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Plexus Corp. | [View](https://www.openjobs-ai.com/jobs/inline-trainer-2nd-shift-neenah-wi-140353441103872480) |
| Commercial Lines Regional Marketing Leader | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/64/3530692d1a06230c2f4532b2f23e5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> USI Insurance Services | [View](https://www.openjobs-ai.com/jobs/commercial-lines-regional-marketing-leader-fort-worth-tx-140353441103872481) |
| Veterinary Cardiologist Interested in Ownership | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/24/829abf09016ee87ad2c7aa780c93f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arista Advanced Pet Care | [View](https://www.openjobs-ai.com/jobs/veterinary-cardiologist-interested-in-ownership-saint-johns-fl-140353441103872482) |
| Entry-Level Account Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/36/afaf02c9a54caff1bd8d9efd73885.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> First Family Insurance | [View](https://www.openjobs-ai.com/jobs/entry-level-account-representative-fort-lauderdale-fl-140353441103872483) |
| 2nd Shift Production Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/3d/082c3623f874004509ed46419b8b0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ATC | [View](https://www.openjobs-ai.com/jobs/2nd-shift-production-supervisor-oklahoma-city-ok-140353441103872484) |
| Day Camp Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/ba/a7193805e61d3c1356418155260ac.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> YMCA of Honolulu | [View](https://www.openjobs-ai.com/jobs/day-camp-director-waialua-hi-140353441103872485) |
| Registered Nurse Operating Room | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/06/5f01f146c8850bf3dd0596b153eb5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HCA HealthONE | [View](https://www.openjobs-ai.com/jobs/registered-nurse-operating-room-denver-co-140353441103872486) |
| Tax Accountant - 2+ Yrs Paid Tax Experience Required | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/tax-accountant-2-yrs-paid-tax-experience-required-boise-id-140353441103872487) |
| Seasonal Business Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-expert-oakhurst-nj-140353441103872488) |
| Seasonal Business Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-expert-smyrna-ga-140353441103872489) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enrolled Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enrolled-agent-or-practicing-attorney-seasonal-remote-chambersburg-pa-140353441103872490) |
| Seasonal Credentialed Tax Expert - Bilingual Spanish | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-tax-expert-bilingual-spanish-clifton-va-140353441103872491) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-ridgeland-ms-140353441103872492) |
| Seasonal Bilingual Credentialed Tax Professional - Remote | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-remote-polk-city-fl-140353441103872493) |
| Work From Home Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/work-from-home-bilingual-tax-professional-cpa-seasonal-vineyard-ut-140353441103872494) |
| Seasonal Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA or EA | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-expert-cpa-or-ea-work-from-home-st-augustine-fl-140353441103872495) |
| Seasonal Credentialed Tax Expert - Bilingual Spanish | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-tax-expert-bilingual-spanish-hollis-nh-140353441103872496) |
| Retail Merchandising Specialist - Capitola, CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/3e/931944873e265c6c2d349198f80d7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Beauty Barrage | [View](https://www.openjobs-ai.com/jobs/retail-merchandising-specialist-capitola-ca-capitola-ca-140353441103872497) |
| Registered Nurse Operating Room II, Pool - Massachusetts Avenue Surgery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/80/64c9a804b9a94c4126a73d50d99f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SCA Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-operating-room-ii-pool-massachusetts-avenue-surgery-bethesda-md-140353441103872498) |
| Regional Safety Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/7d/8b457ef20369d99ffad2d2c804aad.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Accelevation LLC | [View](https://www.openjobs-ai.com/jobs/regional-safety-manager-dallas-tx-140353441103872499) |
| Tax Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Onsite | [View](https://www.openjobs-ai.com/jobs/tax-associate-onsite-2-yrs-paid-tax-experience-required-portland-or-140353441103872500) |
| Tax Preparer - 2+ Yrs Paid Tax Experience Required | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/tax-preparer-2-yrs-paid-tax-experience-required-arizona-city-az-140353441103872501) |
| Seasonal Tax Associate - Work from Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-associate-work-from-home-washington-ut-140353441103872502) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-seasonal-remote-fort-lauderdale-fl-140353441103872503) |
| Seasonal Business Tax Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-associate-fort-collins-co-140353441103872504) |
| Seasonal Business Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-expert-logansport-in-140353441103872505) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-remote-ridgeland-ms-140353441103872506) |
| Work From Home Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/work-from-home-bilingual-tax-professional-cpa-seasonal-killen-al-140353441103872507) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-remote-meridian-id-140353441103872508) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-tacoma-wa-140353441103872509) |
| Seasonal Bilingual Credentialed Tax Professional - Remote | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-remote-tuscaloosa-al-140353441103872510) |
| Seasonal Credentialed Tax Expert - Bilingual Spanish | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-tax-expert-bilingual-spanish-westville-in-140353441103872511) |
| Senior Director, Product Design | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/e7/ac92e246ea43f1da60947282750b0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Strava | [View](https://www.openjobs-ai.com/jobs/senior-director-product-design-san-francisco-ca-140353441103872512) |
| RN Case Manager -  Inpatient Care Coordination | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/0f/ea3112f6a58ec5216ab24a1f3e551.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Presbyterian Healthcare Services | [View](https://www.openjobs-ai.com/jobs/rn-case-manager-inpatient-care-coordination-albuquerque-nm-140353441103872513) |
| Program Specialist, Great Plains-26035 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/28/48a8b439f6dd9f20649ecd6e7a36d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> World Wildlife Fund | [View](https://www.openjobs-ai.com/jobs/program-specialist-great-plains-26035-bozeman-mt-140353441103872514) |
| Production Technician I - Prep 1st Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/00/08a97671ffc2200c92a188e4f5fcd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Quva | [View](https://www.openjobs-ai.com/jobs/production-technician-i-prep-1st-shift-bloomsbury-nj-140353441103872515) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-austin-tx-140353441103872516) |
| Asesor fiscal Bilingual acreditado: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/asesor-fiscal-bilingual-acreditado-cpa-or-ea-or-abogado-practicante-minneapolis-mn-140353441103872517) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-mesquite-tx-140353441103872518) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enrolled Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enrolled-agent-or-practicing-attorney-seasonal-remote-knoxville-tn-140353441103872519) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-clyde-oh-140353441103872520) |
| Seasonal Bilingual Tax Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-tax-professional-cpa-work-from-home-los-angeles-ca-140353441103872521) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-gordonville-pa-140353441103872522) |
| RN-72 Hour | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/b4/ef38cfcf3bde4fe4c5376fb9d518f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Covenant Health | [View](https://www.openjobs-ai.com/jobs/rn-72-hour-oak-ridge-tn-140353441103872523) |
| OB Tech, Labor & Delivery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/ob-tech-labor-delivery-berkeley-ca-140353441103872524) |
| FOREMAN / PAINT & INSULATE | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/93/c9904b5532fd8bc32e6dddb65d2f2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HII | [View](https://www.openjobs-ai.com/jobs/foreman-paint-insulate-goose-creek-sc-140353441103872525) |
| Assistant Director of Nursing (ADON) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/f8/c245b77c4a0f50ef2191e437f0bd7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Monarch Healthcare Management | [View](https://www.openjobs-ai.com/jobs/assistant-director-of-nursing-adon-roseville-mn-140353441103872526) |
| Community Branch Leader | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/08/1ff14448618499fe2fa20a4231fee.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Canvas Credit Union | [View](https://www.openjobs-ai.com/jobs/community-branch-leader-fort-collins-co-140353441103872527) |
| Tax Accountant - 2+ Yrs Paid Tax Experience Required | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/tax-accountant-2-yrs-paid-tax-experience-required-eugene-or-140353441103872528) |
| Tax Expert - Onsite | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/tax-expert-onsite-pittsburgh-pa-140353441103872529) |
| Seasonal Business Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-expert-west-palm-beach-fl-140353441103872530) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-baton-rouge-la-140353441103872531) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-hollis-nh-140353441103872532) |
| Seasonal Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA or EA | [View](https://www.openjobs-ai.com/jobs/seasonal-tax-expert-cpa-or-ea-work-from-home-north-little-rock-ar-140353441103872533) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enroll Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enroll-agent-or-practicing-attorney-seasonal-remote-fort-lauderdale-fl-140353441103872534) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-remote-west-palm-beach-fl-140353441103872535) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-chicago-il-140353441103872536) |
| Seasonal Credentialed Bilingual Tax Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/seasonal-credentialed-bilingual-tax-advisor-cpa-work-from-home-rindge-nh-140353441103872537) |
| Seasonal Business Tax Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-associate-tualatin-or-140353441103872538) |
| Psychiatric Nurse Practitioner (PMHNP) - Telehealth | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/80/c60bbe7fc6d1479bab3aa452f1e18.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brightside Health | [View](https://www.openjobs-ai.com/jobs/psychiatric-nurse-practitioner-pmhnp-telehealth-young-az-140353441103872539) |
| Teller | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/c9/b2f926cb891bb4fb8c191cb8ef8b3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> First Commonwealth Bank | [View](https://www.openjobs-ai.com/jobs/teller-new-castle-pa-140353441103872540) |
| Unit Secretary - Stepdown Unit | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/00/1511322ed0675a3189328643615a3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WVU Medicine | [View](https://www.openjobs-ai.com/jobs/unit-secretary-stepdown-unit-weirton-wv-140353441103872541) |
| Clinical Nurse Educator III, ICU | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/clinical-nurse-educator-iii-icu-burlingame-ca-140353441103872542) |
| Licensed Physical Therapist PT - Care Coordination | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/3c/025dcea235a4bb96cdf34e88cf7aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EmpowerMe Wellness | [View](https://www.openjobs-ai.com/jobs/licensed-physical-therapist-pt-care-coordination-ellisville-mo-140353441103872543) |
| IT Infrastructure Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/c8/f489df014f644d6c57c436136760f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Westlake Financial | [View](https://www.openjobs-ai.com/jobs/it-infrastructure-manager-los-angeles-ca-140353441103872544) |
| Seasonal Business Tax Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-business-tax-associate-cincinnati-oh-140353441103872545) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-seasonal-remote-waianae-hi-140353441103872546) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enrolled Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enrolled-agent-or-practicing-attorney-seasonal-remote-port-st-lucie-fl-140353441103872547) |
| Bilingual Spanish Tax Expert | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CPA, Enroll Agent or Practicing Attorney | [View](https://www.openjobs-ai.com/jobs/bilingual-spanish-tax-expert-cpa-enroll-agent-or-practicing-attorney-seasonal-remote-west-palm-beach-fl-140353441103872548) |
| Seasonal Bilingual Credentialed Tax Professional - Work From Home | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/seasonal-bilingual-credentialed-tax-professional-work-from-home-dubuque-ia-140353441103872549) |
| Profesional Bilingue de Impuestos: CPA or EA or Abogado Practicante | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/89/affb34da2473bbed191c8c8a82b92.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Intuit | [View](https://www.openjobs-ai.com/jobs/profesional-bilingue-de-impuestos-cpa-or-ea-or-abogado-practicante-beecher-il-140353441103872550) |

<p align="center">
  <em>...and 383 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 28, 2026
</p>
