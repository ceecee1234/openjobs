<p align="center">
  <img src="https://img.shields.io/badge/jobs-751+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-426+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 426+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 322 |
| Healthcare | 142 |
| Management | 126 |
| Sales | 65 |
| Engineering | 60 |
| Finance | 22 |
| Operations | 7 |
| Marketing | 4 |
| HR | 3 |

**Top Hiring Companies:** PwC, Jobot, Interstate Companies, Inc., Medcor, OFSAA Solution Architect

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
│  │ Sitemap     │   │ (751+ jobs) │   │ (README + HTML)     │   │
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
- **And 426+ other companies**

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
  <em>Updated March 13, 2026 · Showing 200 of 751+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| BSA Compliance Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/96/1e0701f361b54d26ffe840960a69b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dexian | [View](https://www.openjobs-ai.com/jobs/bsa-compliance-analyst-santa-rosa-ca-145065137668096012) |
| Operations Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f6/2f779f306b678db83662402ee1584.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Corporate Interiors, Inc. | [View](https://www.openjobs-ai.com/jobs/operations-assistant-new-castle-de-145065309634560000) |
| Network Deployment Lead, DC Communities | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/17/f09b91594e1b16f374b34593d895d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amazon Web Services (AWS) | [View](https://www.openjobs-ai.com/jobs/network-deployment-lead-dc-communities-mesa-az-145065309634560001) |
| PATIENT FOOD SERVICES MANAGER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/d2/8f5e19e1aaafa180f7e8a30a37404.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Compass Healthcare | [View](https://www.openjobs-ai.com/jobs/patient-food-services-manager-chicago-il-145065309634560002) |
| Territory Manager - Boston, Rhode Island | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/29/bfca66b4d378507b52afbf9a27bd3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PPG | [View](https://www.openjobs-ai.com/jobs/territory-manager-boston-rhode-island-boston-ma-145065309634560003) |
| Transitions Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/42/2a22f2e55ad9e9fc47e53fb7ce55c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Integrity | [View](https://www.openjobs-ai.com/jobs/transitions-manager-urbandale-ia-145065309634560004) |
| Project Manager - Low Voltage Cabling | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/46/6101567927a759469f6904b0a7c44.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IES Communications | [View](https://www.openjobs-ai.com/jobs/project-manager-low-voltage-cabling-des-moines-ia-145065309634560005) |
| Commercial Lines Account Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/08/7703881398bd4c689aa81520c97e4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> World Insurance Associates LLC | [View](https://www.openjobs-ai.com/jobs/commercial-lines-account-manager-burlington-ia-145065309634560006) |
| Walk-In Wednesday | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/46/958f72a63db50cfff148d22d7d7c4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Avir Health Group | [View](https://www.openjobs-ai.com/jobs/walk-in-wednesday-dripping-springs-tx-145065309634560007) |
| LPN Nurse Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/37/fbd55bab4090c66e106bd751a9ebc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Comprehensive Treatment Centers | [View](https://www.openjobs-ai.com/jobs/lpn-nurse-supervisor-pinehurst-nc-145065309634560008) |
| Biomedical Equipment Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/0d/cd8797fca6888b7f7f26d25e6624d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fresenius Medical Care | [View](https://www.openjobs-ai.com/jobs/biomedical-equipment-technician-aiken-sc-145065460629504000) |
| VP of Sales (OTE $300,000/year USD), @CXT Software | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/1b/eb797639cdbc828c8e0bfbdce6992.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CXT Software | [View](https://www.openjobs-ai.com/jobs/vp-of-sales-ote-300000year-usd-cxt-software-nashville-tn-145065460629504001) |
| Certified Medical Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/b5/cbe91507c445fd5ec8534fc2eeb50.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bucks County Orthopedic Specialists | [View](https://www.openjobs-ai.com/jobs/certified-medical-assistant-doylestown-pa-145065460629504002) |
| Hybrid Cloud & Tech Resilience - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/hybrid-cloud-tech-resilience-manager-charlotte-nc-145065582264320000) |
| AI First Software Engineer - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ai-first-software-engineer-senior-associate-jacksonville-fl-145065582264320001) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/af/e82514c1d9c6e54f1826b5b43d961.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MyShyft | [View](https://www.openjobs-ai.com/jobs/registered-nurse-springfield-il-145063023738880597) |
| Financial Advisor - Career Changer Opportunity! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/70/26ca5c56fb5bb7d8f7585e225dc78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Principal Financial Group | [View](https://www.openjobs-ai.com/jobs/financial-advisor-career-changer-opportunity-grand-rapids-mi-145063023738880598) |
| Behavior Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/12/60842cb2b0da3409c92f71fe9e22d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Centria Autism | [View](https://www.openjobs-ai.com/jobs/behavior-technician-silver-spring-md-145063023738880599) |
| Behavior Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/12/60842cb2b0da3409c92f71fe9e22d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Centria Autism | [View](https://www.openjobs-ai.com/jobs/behavior-technician-frisco-tx-145063023738880600) |
| Client Relationship Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/e2/be0857a197f5f173a7a8fb80dcf25.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SolomonEdwards | [View](https://www.openjobs-ai.com/jobs/client-relationship-associate-pittsburgh-pa-145063023738880601) |
| Math Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/c7/259c7b286453abccf6f87ed3915f7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Middle School | [View](https://www.openjobs-ai.com/jobs/math-teacher-middle-school-2627-anthem-az-145063023738880602) |
| Machine Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/8d/0cd01a69911faa676bddaded37426.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Manpower San Diego | [View](https://www.openjobs-ai.com/jobs/machine-operator-temecula-ca-145063023738880603) |
| Environmental Services Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/3b/a797e9b6f2c34d53973e1bb007f72.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Salvation Army | [View](https://www.openjobs-ai.com/jobs/environmental-services-associate-philadelphia-pa-145063023738880604) |
| Legal Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/04/e341b3160d4a365ebfa980e7fc91a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Robert Half | [View](https://www.openjobs-ai.com/jobs/legal-assistant-san-jose-ca-145063023738880605) |
| Retirement Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/85/6310e2e443e53f0f48d57b31e9e1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SkyKey Financial | [View](https://www.openjobs-ai.com/jobs/retirement-specialist-north-lynnwood-wa-145063023738880606) |
| Remote Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a4/fc0e823af041d7fa9b9a784133731.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Entry Level | [View](https://www.openjobs-ai.com/jobs/remote-sales-representative-entry-level-part-time-or-full-time-toledo-oh-145063023738880607) |
| Remote Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a4/fc0e823af041d7fa9b9a784133731.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Entry Level | [View](https://www.openjobs-ai.com/jobs/remote-sales-representative-entry-level-part-time-or-full-time-pittsburgh-pa-145063023738880608) |
| Environmental Remediation Project Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/35/29c8a34b195a7aa7f437c5a17d41d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EnSafe | [View](https://www.openjobs-ai.com/jobs/environmental-remediation-project-engineer-pensacola-fl-145063023738880609) |
| Patient Care Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/2e/3527f51f437627c86960f0189c480.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HearingLife | [View](https://www.openjobs-ai.com/jobs/patient-care-coordinator-orleans-ma-145063023738880610) |
| Outpatient Psychiatrist - Downtown Atlanta | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e1/9fd4101308d204a2b21fae0728634.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Geode Health | [View](https://www.openjobs-ai.com/jobs/outpatient-psychiatrist-downtown-atlanta-atlanta-ga-145063023738880611) |
| Clinical Partnerships Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/1a/05474cd4d12faf2ad2d8276e1861d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Banting AI | [View](https://www.openjobs-ai.com/jobs/clinical-partnerships-lead-united-states-145063023738880612) |
| Warehouser | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9f/df5b5a99f71763a5a896bc94df96e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> H.B. Fuller | [View](https://www.openjobs-ai.com/jobs/warehouser-michigan-center-mi-145063023738880613) |
| Application Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/70/ed1f61e9314f924e9298a564bba79.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Thermon | [View](https://www.openjobs-ai.com/jobs/application-engineer-knoxville-metropolitan-area-145063023738880615) |
| Business Intelligence Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/30/b06b9907198d68f229aeb3e8430cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insight Global | [View](https://www.openjobs-ai.com/jobs/business-intelligence-analyst-stamford-ct-145063023738880616) |
| Retirement Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/85/6310e2e443e53f0f48d57b31e9e1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SkyKey Financial | [View](https://www.openjobs-ai.com/jobs/retirement-specialist-prairie-village-ks-145063023738880617) |
| Revenue Integrity Liaison | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/16/eb7f343d8c9142856d7ab257ea40a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MUSC Health | [View](https://www.openjobs-ai.com/jobs/revenue-integrity-liaison-charleston-sc-145063023738880618) |
| Veterinary Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/d7/0e1516c2c8f18adece0ce0cb315a4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alliance Animal Health | [View](https://www.openjobs-ai.com/jobs/veterinary-assistant-little-rock-metropolitan-area-145063023738880619) |
| Veterinary Receptionist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/d7/0e1516c2c8f18adece0ce0cb315a4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alliance Animal Health | [View](https://www.openjobs-ai.com/jobs/veterinary-receptionist-des-moines-metropolitan-area-145063023738880620) |
| Retirement Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/85/6310e2e443e53f0f48d57b31e9e1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SkyKey Financial | [View](https://www.openjobs-ai.com/jobs/retirement-specialist-ashland-ca-145063023738880621) |
| Sales Development Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/d1/84694fdaca025c0e6aef3581d5fc0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Martindale-Avvo | [View](https://www.openjobs-ai.com/jobs/sales-development-representative-alameda-county-ca-145063023738880622) |
| Mental Health Worker III - LVN or LPT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/mental-health-worker-iii-lvn-or-lpt-sacramento-ca-145063023738880623) |
| Behavior Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/12/60842cb2b0da3409c92f71fe9e22d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Work with Kids | [View](https://www.openjobs-ai.com/jobs/behavior-technician-work-with-kids-training-provided-albuquerque-nm-145063023738880624) |
| Senior Manager - Service | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/22/178760ed73d98ad024e8d11cd1f09.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dürr | [View](https://www.openjobs-ai.com/jobs/senior-manager-service-southfield-mi-145063023738880625) |
| Business Process Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/27/1e06f8b4f18c9d48636037d201716.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tekgence Inc | [View](https://www.openjobs-ai.com/jobs/business-process-consultant-hartford-ct-145063023738880626) |
| Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/88/0afb83bc6edf9e04df13444d8680d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brooksource | [View](https://www.openjobs-ai.com/jobs/technician-lumpkin-county-ga-145063023738880627) |
| Retirement Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/85/6310e2e443e53f0f48d57b31e9e1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SkyKey Financial | [View](https://www.openjobs-ai.com/jobs/retirement-specialist-summit-nj-145063023738880628) |
| Social Media Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/fc/486541d3adbae1202abf992bb3cfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MMGY Global | [View](https://www.openjobs-ai.com/jobs/social-media-intern-culver-city-ca-145063023738880629) |
| Remote Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a4/fc0e823af041d7fa9b9a784133731.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Entry Level | [View](https://www.openjobs-ai.com/jobs/remote-sales-representative-entry-level-part-time-or-full-time-wichita-ks-145063023738880630) |
| Technical Business Analyst, Lead Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/be/3b7cdaa57df4339897f4068aa971f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lovelytics | [View](https://www.openjobs-ai.com/jobs/technical-business-analyst-lead-consultant-arlington-va-145063023738880631) |
| Product Marketing Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/8d/8d508b5edeccfb126dab97baab31d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> groundcover | [View](https://www.openjobs-ai.com/jobs/product-marketing-manager-san-francisco-ca-145063023738880632) |
| Certified Nurse Practitioner***Weekends*** | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/7e/f85a8db553c2034271f93496e1268.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Altea Healthcare | [View](https://www.openjobs-ai.com/jobs/certified-nurse-practitionerweekends-east-lansing-mi-145063023738880633) |
| Hospice Registered Nurse (35573) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/37/a03ad1ad5e5d7d6c29bfd0d5648b3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Care Team | [View](https://www.openjobs-ai.com/jobs/hospice-registered-nurse-35573-reading-pa-145063023738880634) |
| Telecommunications Systems Engineer – Facilities & Towers | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/ea65508b092df5e5657c7004f804a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TPI Global Solutions | [View](https://www.openjobs-ai.com/jobs/telecommunications-systems-engineer-facilities-towers-los-angeles-ca-145063023738880635) |
| Advertising Sales Manager, Finance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/07/12e635aa83b3592a97eb1b24355b3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> U.S. News & World Report | [View](https://www.openjobs-ai.com/jobs/advertising-sales-manager-finance-new-york-ny-145063023738880636) |
| Site Safety Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2f/4335df452f25ec309144bb03a923b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> FootBridge | [View](https://www.openjobs-ai.com/jobs/site-safety-manager-rayville-la-145063023738880639) |
| Digital Specialist I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/18/52e52d8d3b617c3cd576a3e48ac9c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> First Bank (FBNC) | [View](https://www.openjobs-ai.com/jobs/digital-specialist-i-cary-nc-145063023738880640) |
| Aerospace Quality Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/e6/41c923ebdfc4d816d028abcb5f9d8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hytek Finishes Co. | [View](https://www.openjobs-ai.com/jobs/aerospace-quality-engineer-kent-wa-145063023738880641) |
| Warehouse Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/b3/97d92bdbc6a6cf12f4841320ca4a5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bimbo Bakeries USA | [View](https://www.openjobs-ai.com/jobs/warehouse-associate-pooler-ga-145063023738880642) |
| Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/e7/649f7c0ca4dd77c34338d1a7def29.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Team Rehabilitation Physical Therapy | [View](https://www.openjobs-ai.com/jobs/physical-therapist-macomb-township-mi-145063023738880643) |
| Summer Math, English & ASL Instructor- Ripon College | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7a/627404b9dbac66384dfae7b707ff1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Forward Service Corporation | [View](https://www.openjobs-ai.com/jobs/summer-math-english-asl-instructor-ripon-college-wautoma-wi-145063023738880644) |
| Dietary Aide | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/03/ca48e5138d24c96ebfad349be3d50.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CHR Consulting Services, Inc. | [View](https://www.openjobs-ai.com/jobs/dietary-aide-uniontown-pa-145063023738880645) |
| Tax Supervisor – Public Accounting (Hybrid) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/cf/224f918b5bf13e4599a509d784ad2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Analytix Solutions | [View](https://www.openjobs-ai.com/jobs/tax-supervisor-public-accounting-hybrid-wakefield-ma-145063023738880647) |
| Unified Communication Analyst I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/4e/45d32cc468dcd7131f59d5bcbdbb0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Baptist Health | [View](https://www.openjobs-ai.com/jobs/unified-communication-analyst-i-montgomery-al-145063023738880648) |
| Oracle MDM Consultant - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdm-consultant-senior-associate-sacramento-ca-145063023738880649) |
| Oracle MDM Consultant - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdm-consultant-senior-associate-stamford-ct-145063023738880650) |
| Oracle Cloud Analytics (FDI/FAW) - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cloud-analytics-fdifaw-manager-rochester-ny-145063023738880651) |
| Associate Creative Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/16/2806b1f6bc441591000ae87f350f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aquent | [View](https://www.openjobs-ai.com/jobs/associate-creative-director-houston-tx-145063023738880653) |
| Senior Human Resources Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/1c/46f4fee6d8533bee4af059257e24f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Movement Search & Delivery | [View](https://www.openjobs-ai.com/jobs/senior-human-resources-manager-indiana-united-states-145063023738880654) |
| Production Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/b7/1e29c50c405b74041682a9c6e43b7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Flexible Products | [View](https://www.openjobs-ai.com/jobs/production-supervisor-chaska-mn-145063023738880656) |
| Vice President of Technology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/87/b918fe8c7b4a429ce8d6149eaab07.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Attractivate Consulting Solutions | [View](https://www.openjobs-ai.com/jobs/vice-president-of-technology-houston-tx-145063023738880657) |
| Branch Office Administrator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/82/2407c4cb46235f6ff6cdd3e254fbe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bankers Life | [View](https://www.openjobs-ai.com/jobs/branch-office-administrator-cape-girardeau-mo-145063023738880658) |
| Database Administrator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/75/f132cb1dd5c63066aa62ed5383939.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LTIMindtree | [View](https://www.openjobs-ai.com/jobs/database-administrator-edison-nj-145063023738880659) |
| Project Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/28/124b8385707ccc3b97ae294502fab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Harper Harrison | [View](https://www.openjobs-ai.com/jobs/project-executive-dallas-fort-worth-metroplex-145063023738880660) |
| Property Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/ae/0648bdce459dd2acac5affc6ccb8b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Chief Seattle Club | [View](https://www.openjobs-ai.com/jobs/property-manager-seattle-wa-145063023738880661) |
| Mental Health Worker III - LVN or LPT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fe/df04cde512524c8fe8e2c303a1cb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sutter Health | [View](https://www.openjobs-ai.com/jobs/mental-health-worker-iii-lvn-or-lpt-sacramento-ca-145063023738880662) |
| Concierge Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/c0/797b5799b1e85445b321fa6fc78d4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Boston Consulting Group (BCG) | [View](https://www.openjobs-ai.com/jobs/concierge-assistant-miami-fl-145063023738880663) |
| Mortgage Processor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/af/e0a4168fcfb615f75865fdd3ff233.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 1st State Bank Great Lakes Bay | [View](https://www.openjobs-ai.com/jobs/mortgage-processor-saginaw-mi-145063023738880664) |
| Senior Validation Engineering Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/03/2985495f95cc52b29cc007b4e56ea.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OSI Engineering | [View](https://www.openjobs-ai.com/jobs/senior-validation-engineering-manager-johns-creek-ga-145063023738880665) |
| Frontend Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0a/509dc5444d7774dd17e310d619820.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Haystack | [View](https://www.openjobs-ai.com/jobs/frontend-developer-washington-dc-baltimore-area-145063023738880666) |
| Social Service Clinician I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/4e/d7bcae71fc87e78633553e2654be8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Commonwealth of Kentucky | [View](https://www.openjobs-ai.com/jobs/social-service-clinician-i-west-liberty-ky-145063023738880667) |
| HHA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/b3/7d6252a68c4601893ec030be5d2c3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> White Glove Community Care | [View](https://www.openjobs-ai.com/jobs/hha-staten-island-ny-145063023738880668) |
| Registered Nurse, R.N. | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/73/9b08bf036f7af641b7b2c38ab385e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Accolade Healthcare | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-waterloo-il-145063023738880669) |
| Support Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/34/d9a784f8c2dd342b4d9dba29a7388.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TriNetX | [View](https://www.openjobs-ai.com/jobs/support-engineer-cambridge-ma-145063023738880670) |
| Fund Accountant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/93/05c5ffeeb4e15c93719c32272e526.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CTP | [View](https://www.openjobs-ai.com/jobs/fund-accountant-united-states-145063023738880671) |
| Operator I - C | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e8/2cb93172f21339bbcb27b5d6f063d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Samuel, Son & Co. | [View](https://www.openjobs-ai.com/jobs/operator-i-c-irving-tx-145063023738880673) |
| Oracle MDM Consultant - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdm-consultant-senior-associate-boston-ma-145063023738880674) |
| Oracle Cloud Analytics (FDI/FAW) - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cloud-analytics-fdifaw-manager-san-antonio-tx-145063023738880675) |
| Oracle MDM/CDM Solution Lead - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdmcdm-solution-lead-manager-cincinnati-oh-145063023738880676) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Architect | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-architect-manager-miami-fl-145063023738880677) |
| Data Strategy [Insurance]- Experienced Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/data-strategy-insurance-experienced-associate-louisville-ky-145063023738880678) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Design | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-design-senior-associate-boston-ma-145063023738880679) |
| Director, Travel Experiences Marketing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/3c/e5df4a6b95d049b47c7d6b67e7c4b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Visa | [View](https://www.openjobs-ai.com/jobs/director-travel-experiences-marketing-san-francisco-ca-145063023738880680) |
| Data Strategy [Insurance]- Experienced Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/data-strategy-insurance-experienced-associate-des-moines-ia-145063023738880681) |
| SAP Integrated Business Planning (IBP) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-integrated-business-planning-ibp-senior-manager-los-angeles-ca-145063023738880682) |
| Retirement Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/85/6310e2e443e53f0f48d57b31e9e1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SkyKey Financial | [View](https://www.openjobs-ai.com/jobs/retirement-specialist-bayou-cane-la-145063023738880683) |
| SAP Integrated Business Planning (IBP) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-integrated-business-planning-ibp-senior-manager-montpelier-vt-145063023738880684) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Architect | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-architect-manager-st-louis-mo-145063023738880685) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Architect | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-architect-manager-melville-ny-145063023738880686) |
| Oracle Cloud Analytics (FDI/FAW) - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cloud-analytics-fdifaw-senior-associate-fayetteville-ar-145063023738880687) |
| Salesforce CPQ/Revenue Cloud - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/salesforce-cpqrevenue-cloud-senior-associate-houston-tx-145063023738880688) |
| Registered Nurse (RN) Emergency | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/fd/87e099ca4630b42393bb3f9f936c9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trinity Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-emergency-grand-haven-mi-145063023738880689) |
| Driver/Rigger | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/33/dbed17fad1c4f0ae227cfeb0b668a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mazzella | [View](https://www.openjobs-ai.com/jobs/driverrigger-longview-tx-145063023738880690) |
| Psychiatric Nurse Practitioner/Physician Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/50/5a89940b63659a284e3cb7973b7cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Eventus WholeHealth | [View](https://www.openjobs-ai.com/jobs/psychiatric-nurse-practitionerphysician-assistant-rutherfordton-nc-145063023738880691) |
| Senior Investigator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/3f/808f7d0899bf66011c2d825e16716.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Massachusetts Department of Developmental Services | [View](https://www.openjobs-ai.com/jobs/senior-investigator-wrentham-ma-145063023738880692) |
| Senior Business Intelligence Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/d8/0fad6df8a5bc425be5d2c721d69f7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tryfacta, Inc. | [View](https://www.openjobs-ai.com/jobs/senior-business-intelligence-developer-washington-dc-145063023738880693) |
| Ambulatory Nurse II - Robbinsville | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/97/3fdfec10c6f726b11f273488ad009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Penn Medicine, University of Pennsylvania Health System | [View](https://www.openjobs-ai.com/jobs/ambulatory-nurse-ii-robbinsville-robbinsville-nj-145063023738880694) |
| Bilingual Registered Dietician Clinical Trials Telehealth | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/49/74f8eed435f594de307c71ed324e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Per Diem | [View](https://www.openjobs-ai.com/jobs/bilingual-registered-dietician-clinical-trials-telehealth-per-diem-florida-melbourne-fl-145063023738880695) |
| Provider Network Contractor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/b1/a8291af4ebf5b2c99089a590506b0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Colorado Access | [View](https://www.openjobs-ai.com/jobs/provider-network-contractor-denver-co-145063023738880696) |
| Account Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/b3/010eb1303ae6213ac5c92e097b4ef.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WebMD | [View](https://www.openjobs-ai.com/jobs/account-executive-united-states-145063023738880698) |
| Behavior Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/12/60842cb2b0da3409c92f71fe9e22d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Centria Autism | [View](https://www.openjobs-ai.com/jobs/behavior-technician-fort-worth-tx-145063023738880699) |
| IT Support Technician Must live in WA ($50K-$60K, Entry Level w/ Degree | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/f2/0d9b408bbcf75d7ce3af7c05451ca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> #twiceasnice Recruiting | [View](https://www.openjobs-ai.com/jobs/it-support-technician-must-live-in-wa-50k-60k-entry-level-w-degree-washington-united-states-145063023738880700) |
| Adult Day Program Assistant - 1st shift M-F | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/1f/f284bfaf5fbe99d47da34b8f90886.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Twin Lakes Community | [View](https://www.openjobs-ai.com/jobs/adult-day-program-assistant-1st-shift-m-f-burlington-nc-145063023738880702) |
| Machine Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/69/e2c10df8d778d999029d843f3b82b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Technical Associates | [View](https://www.openjobs-ai.com/jobs/machine-operator-martinsburg-wv-145063023738880703) |
| Laboratory Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/30/b06b9907198d68f229aeb3e8430cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insight Global | [View](https://www.openjobs-ai.com/jobs/laboratory-technician-haverhill-ma-145063023738880704) |
| Scrum Master | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/80/f4f0b6124b7ecfe74e9a8d2df118d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tixy Tech | [View](https://www.openjobs-ai.com/jobs/scrum-master-houston-tx-145063023738880705) |
| PTA Physical Therapist Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/36/df70f591e8ec82d70bd792ba44161.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Grand Healthcare System | [View](https://www.openjobs-ai.com/jobs/pta-physical-therapist-assistant-rochester-ny-145063023738880707) |
| Grant Writer and Award Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/6a/72df1e7946f61dfe8a77a7b8d6f48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Texas Department of State Health Services | [View](https://www.openjobs-ai.com/jobs/grant-writer-and-award-specialist-austin-tx-145063023738880708) |
| Oracle MDM Consultant - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdm-consultant-senior-associate-spartanburg-sc-145063023738880709) |
| Oracle MDM Consultant - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdm-consultant-senior-associate-rosemont-il-145063023738880710) |
| Oracle MDM Consultant - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdm-consultant-senior-associate-irvine-ca-145063023738880711) |
| SAP Integrated Business Planning (IBP) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-integrated-business-planning-ibp-senior-manager-charlotte-nc-145063023738880712) |
| Salesforce CPQ/Revenue Cloud Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/salesforce-cpqrevenue-cloud-manager-hartford-ct-145063023738880713) |
| P&C Commercial Product Owner, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/pc-commercial-product-owner-manager-new-orleans-la-145063023738880714) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Architect | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-architect-manager-little-rock-ar-145063023738880715) |
| Sp Unit Staff RN - Hospital (NICU--Baby Catcher) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/5d/0aac9b091e8a1c001ab78acce07fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente | [View](https://www.openjobs-ai.com/jobs/sp-unit-staff-rn-hospital-nicu-baby-catcher-los-angeles-ca-145063023738880716) |
| PCA I, Geriatric Medical Psych, 32hrs, Evenings | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/fb/de81b7089fc9708df26cf1516e601.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UMass Memorial Health | [View](https://www.openjobs-ai.com/jobs/pca-i-geriatric-medical-psych-32hrs-evenings-clinton-ma-145063023738880717) |
| Appointment/Registration Clerk Must reside on Maui, Island of Hawaii or Oahu. Work from home option is available | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/5d/0aac9b091e8a1c001ab78acce07fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente | [View](https://www.openjobs-ai.com/jobs/appointmentregistration-clerk-must-reside-on-maui-island-of-hawaii-or-oahu-work-from-home-option-is-available-waipahu-hi-145063023738880718) |
| Human Resources & Operations Director- US | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/df/d2f3f786fdd8bbd85c2eef20c0abf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Zenwork, Inc | [View](https://www.openjobs-ai.com/jobs/human-resources-operations-director-us-fayetteville-ar-145063023738880719) |
| Concierge, Hope Lodge | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/55/0c64ae465f9a20995a80f110eab5c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sun | [View](https://www.openjobs-ai.com/jobs/concierge-hope-lodge-sun-tues-300pm-1100pm-burlington-vt-145063023738880720) |
| Physical Therapy Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/f2/ff2ed3c83c3c5ce510c4666f6fb0d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PRN | [View](https://www.openjobs-ai.com/jobs/physical-therapy-assistant-prn-mercy-jefferson-festus-mo-145063023738880721) |
| Senior Director of Customer Strategy and Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f1/98913aa5a4af6a0927aefd965d785.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Skan AI | [View](https://www.openjobs-ai.com/jobs/senior-director-of-customer-strategy-and-operations-charlotte-nc-145063023738880722) |
| Senior Business Analyst (Data & Systems Analysis) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/f6/a22cd90eb05d92793002e712c9dbf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CrowdPlat | [View](https://www.openjobs-ai.com/jobs/senior-business-analyst-data-systems-analysis-austin-texas-metropolitan-area-145063023738880723) |
| Technician, Maintenance II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/62/4484fa865421f0d1762bacfb680bb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NOVONIX | [View](https://www.openjobs-ai.com/jobs/technician-maintenance-ii-chattanooga-tn-145063023738880724) |
| Practice Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/5a/6872a7502dd5235ce1a618fd00f88.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MassMutual Pittsburgh | [View](https://www.openjobs-ai.com/jobs/practice-manager-upper-st-clair-pa-145063023738880725) |
| Retirement Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/85/6310e2e443e53f0f48d57b31e9e1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SkyKey Financial | [View](https://www.openjobs-ai.com/jobs/retirement-specialist-oakdale-ca-145063023738880726) |
| Inside Sales Business Development Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9f/df5b5a99f71763a5a896bc94df96e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> H.B. Fuller | [View](https://www.openjobs-ai.com/jobs/inside-sales-business-development-representative-st-paul-mn-145063023738880727) |
| Research Analyst/Report Writer, Fraud Management (Remote) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/d9/ae568c569570e24900e746b592c3c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Escalent | [View](https://www.openjobs-ai.com/jobs/research-analystreport-writer-fraud-management-remote-united-states-145063023738880728) |
| Lead Salesforce Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/72/c5ea36d1d8ee5a8b61842dd368dff.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Programmers.io | [View](https://www.openjobs-ai.com/jobs/lead-salesforce-developer-hartford-ct-145063023738880729) |
| Vice President of Business Development | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/6b/a7664f64d6ed5a5d89522770549b0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Luminary Hospice | [View](https://www.openjobs-ai.com/jobs/vice-president-of-business-development-dallas-tx-145063023738880730) |
| New Paid Movement Study in Jersey City | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/16/5cecfce584c51e706af3e63fe0375.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TransPerfect | [View](https://www.openjobs-ai.com/jobs/new-paid-movement-study-in-jersey-city-clifton-nj-145063023738880731) |
| Practice Manager - Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/97/3fdfec10c6f726b11f273488ad009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Penn Medicine, University of Pennsylvania Health System | [View](https://www.openjobs-ai.com/jobs/practice-manager-per-diem-plumsteadville-pa-145063023738880732) |
| System Administrator / Windows Server Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/c4/3843a3ed189fed12215aa92d4719c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Peterson Technology Partners | [View](https://www.openjobs-ai.com/jobs/system-administrator-windows-server-engineer-dearborn-mi-145063023738880733) |
| Computer Systems Engineer/Architect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/75/f132cb1dd5c63066aa62ed5383939.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LTIMindtree | [View](https://www.openjobs-ai.com/jobs/computer-systems-engineerarchitect-edison-nj-145063023738880734) |
| DWP Service Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/91/1b032481eb442db5bc4f2fc77269e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Siemens Energy | [View](https://www.openjobs-ai.com/jobs/dwp-service-manager-orlando-fl-145063023738880735) |
| Elevator Worker | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/a1/f0e768e9cd3892b289705acad3eea.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Prairie Grain Partners LLC | [View](https://www.openjobs-ai.com/jobs/elevator-worker-miller-sd-145063023738880737) |
| Production Technician (Seattle, WA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/0d/e57f1066206645c85d34ccb055653.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Microbiologique Inc | [View](https://www.openjobs-ai.com/jobs/production-technician-seattle-wa-seattle-wa-145063023738880738) |
| WELDING PROJECT LEADER 2 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/93/c9904b5532fd8bc32e6dddb65d2f2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HII | [View](https://www.openjobs-ai.com/jobs/welding-project-leader-2-newport-news-va-145063023738880739) |
| Home Health Licensed Practical Nurse LPN Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/3b/62a1b0d6aa6119b0ccdf0b2feef99.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aveanna Healthcare | [View](https://www.openjobs-ai.com/jobs/home-health-licensed-practical-nurse-lpn-part-time-duluth-mn-145063023738880740) |
| Internet Installation Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/f2/900b00b91bad8067d32d18be5d7cd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Viaero Wireless | [View](https://www.openjobs-ai.com/jobs/internet-installation-technician-lexington-ne-145063023738880742) |
| Office Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/88/5ea91163fa3577134853a06cf671f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Service Motor Company | [View](https://www.openjobs-ai.com/jobs/office-manager-fond-du-lac-wi-145063023738880743) |
| Service Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/31/2e0eedf7df4a51bcd13b17dac1464.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Greenway Automotive | [View](https://www.openjobs-ai.com/jobs/service-advisor-floyd-county-ga-145063023738880744) |
| HISTOTECHNICIAN-Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/00/599c2cf996628e055a2a386f0feb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Oswego Health | [View](https://www.openjobs-ai.com/jobs/histotechnician-per-diem-oswego-ny-145063023738880745) |
| Aquatics Instructor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/3b/a797e9b6f2c34d53973e1bb007f72.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Salvation Army | [View](https://www.openjobs-ai.com/jobs/aquatics-instructor-philadelphia-pa-145063023738880746) |
| Activity Aide | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/36/df70f591e8ec82d70bd792ba44161.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Grand Healthcare System | [View](https://www.openjobs-ai.com/jobs/activity-aide-ilion-ny-145063023738880749) |
| PRN Clinical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/28/ab38e4a535642201e401d21becd79.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lighthouse Behavioral Health Solutions | [View](https://www.openjobs-ai.com/jobs/prn-clinical-therapist-lima-oh-145063023738880750) |
| Oracle EBS Suite DBA (US Citizen and W2 only) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e9/f852c61cbe7c0b0225d2a217029e7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AppLab Systems, Inc | [View](https://www.openjobs-ai.com/jobs/oracle-ebs-suite-dba-us-citizen-and-w2-only-united-states-145063023738880752) |
| Oracle Cloud Analytics (FDI/FAW) - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cloud-analytics-fdifaw-manager-boston-ma-145063023738880753) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Architect | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-architect-manager-milwaukee-wi-145063023738880754) |
| Oracle MDM/CDM Solution Lead - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdmcdm-solution-lead-manager-dallas-tx-145063023738880755) |
| SAP Extended Warehouse Management (EWM) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-extended-warehouse-management-ewm-senior-manager-rosemont-il-145063023738880756) |
| SAP Integrated Business Planning (IBP) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-integrated-business-planning-ibp-senior-manager-milwaukee-wi-145063023738880757) |
| Territory Sales Representative / Restaurant Specialist - Fayetteville, GA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/ba/61df4c4c6cc216e085c462da163a5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SpotOn | [View](https://www.openjobs-ai.com/jobs/territory-sales-representative-restaurant-specialist-fayetteville-ga-fayetteville-ga-145063023738880758) |
| Salesforce CPQ/Revenue Cloud - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/salesforce-cpqrevenue-cloud-senior-associate-baltimore-md-145063023738880759) |
| SAP Integrated Business Planning (IBP) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-integrated-business-planning-ibp-senior-manager-hartford-ct-145063023738880760) |
| Oracle MDM/CDM Solution Lead - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-mdmcdm-solution-lead-manager-spartanburg-sc-145063023738880761) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Architect | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-architect-manager-salt-lake-city-ut-145063023738880762) |
| Salesforce CPQ/Revenue Cloud - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/salesforce-cpqrevenue-cloud-senior-associate-little-rock-ar-145063023738880763) |
| Field Operations Support Assistant (part-time) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/76/f2c01be007dbd8c7fdb01a4ec6115.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Service Corporation International | [View](https://www.openjobs-ai.com/jobs/field-operations-support-assistant-part-time-georgetown-tx-145063023738880764) |
| Channel Account Manager – West Coast (VAR / K-12 Education) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/36/aa2d51122f827004e568af835d1c6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ASUS | [View](https://www.openjobs-ai.com/jobs/channel-account-manager-west-coast-var-k-12-education-california-united-states-145063023738880765) |
| Athletic Trainer Certified | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/a7/097f40a1560ea706803fdfab543c3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Orthopedics Seacoast Clinic | [View](https://www.openjobs-ai.com/jobs/athletic-trainer-certified-orthopedics-seacoast-clinic-prn-little-river-sc-145063023738880766) |
| Category Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/eb/4edb5f3f2f95284278e36ace77763.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BayOne Solutions | [View](https://www.openjobs-ai.com/jobs/category-manager-san-jose-ca-145063023738880767) |
| Industrial Shop Clerk / Admin ($27-$30 + OT, Order Management & Inventory) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/f2/0d9b408bbcf75d7ce3af7c05451ca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> #twiceasnice Recruiting | [View](https://www.openjobs-ai.com/jobs/industrial-shop-clerk-admin-27-30-ot-order-management-inventory-hammond-in-145063023738880768) |
| Director of Service Management (26-27) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/74/497a4469a90d95de78a185e45b40f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IDEA Public Schools | [View](https://www.openjobs-ai.com/jobs/director-of-service-management-26-27-hidalgo-county-tx-145063023738880769) |
| Business Development Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/30/b06b9907198d68f229aeb3e8430cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insight Global | [View](https://www.openjobs-ai.com/jobs/business-development-manager-california-united-states-145063023738880770) |
| Front Office Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/fb/c7d27fbd188f328894c436486aba4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CB Partners, LLC | [View](https://www.openjobs-ai.com/jobs/front-office-assistant-boston-ma-145063023738880771) |
| Inside Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/78/231424ba44b24aa9194cf458948d9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CarsDirect.com | [View](https://www.openjobs-ai.com/jobs/inside-sales-representative-auburn-hills-mi-145063023738880772) |
| ENGINEERING TECHNICIAN 2 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/93/c9904b5532fd8bc32e6dddb65d2f2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HII | [View](https://www.openjobs-ai.com/jobs/engineering-technician-2-newport-news-va-145063023738880773) |
| Bookkeeper | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/c7/ee29f36cd823a7d19567114e6ddcc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sechler Law Firm, LLC | [View](https://www.openjobs-ai.com/jobs/bookkeeper-warrendale-pa-145063023738880774) |
| Manufacturing Process Engineer – BIW / General Assembly (Bilingual Spanish & English Required) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/88/5e735a328e717c9d6c69d0740500d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Zobility | [View](https://www.openjobs-ai.com/jobs/manufacturing-process-engineer-biw-general-assembly-bilingual-spanish-english-required-auburn-hills-mi-145063023738880775) |
| Corporate Office Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/86/eb9eb2243dcbbeb76433517fa2f99.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sante Group Companies | [View](https://www.openjobs-ai.com/jobs/corporate-office-manager-silver-spring-md-145063023738880776) |
| Claims Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/71/9689c74c60bca0d2c4c6e60eb12ea.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Doctors HealthCare Plans, Inc. | [View](https://www.openjobs-ai.com/jobs/claims-specialist-miami-fl-145063023738880777) |
| Technical Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0a/509dc5444d7774dd17e310d619820.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Haystack | [View](https://www.openjobs-ai.com/jobs/technical-writer-united-states-145063023738880778) |
| Social Worker TEMP Pt | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/ba/ea52fea7db47ad2fbddfa3b825701.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ryders Health Management | [View](https://www.openjobs-ai.com/jobs/social-worker-temp-pt-windham-ct-145063023738880779) |
| Case Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/54/1af9c81af6be7915fde7c89c61ca1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PSYCHIATRIC & BEHAVIORAL SOLUTIONS, L.L.C. | [View](https://www.openjobs-ai.com/jobs/case-manager-salt-lake-city-ut-145063023738880780) |
| Personal Lines Insurance Sales Agent | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/c2/7631d40e844d2293901c26db7ec94.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Farmers Insurance Agencies | [View](https://www.openjobs-ai.com/jobs/personal-lines-insurance-sales-agent-st-louis-mo-145063023738880781) |
| P&C Commercial Product Owner, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/pc-commercial-product-owner-manager-silicon-valley-ca-145063023738880782) |
| Data Strategy [Insurance]- Experienced Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/data-strategy-insurance-experienced-associate-san-antonio-tx-145063023738880783) |
| Oracle Cloud Analytics (FDI/FAW) - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cloud-analytics-fdifaw-manager-indianapolis-in-145063023738880784) |
| Salesforce CPQ/Revenue Cloud Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/salesforce-cpqrevenue-cloud-manager-minneapolis-mn-145063023738880785) |
| SAP Extended Warehouse Management (EWM) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-extended-warehouse-management-ewm-senior-manager-stamford-ct-145063023738880786) |
| SAP Integrated Business Planning (IBP) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-integrated-business-planning-ibp-senior-manager-san-diego-ca-145063023738880787) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Design | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-design-senior-associate-los-angeles-ca-145063023738880788) |
| SAP Extended Warehouse Management (EWM) Senior  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-extended-warehouse-management-ewm-senior-manager-pittsburgh-pa-145063023738880789) |
| Data Strategy [Insurance]- Experienced Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/data-strategy-insurance-experienced-associate-portland-or-145063023738880790) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Design | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-design-senior-associate-melville-ny-145063023738880791) |
| Data Strategy [Insurance]- Experienced Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/data-strategy-insurance-experienced-associate-indianapolis-in-145063023738880792) |
| Oracle | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OFSAA Solution Architect | [View](https://www.openjobs-ai.com/jobs/oracle-ofsaa-solution-architect-manager-tampa-fl-145063023738880793) |
| Regional Sales Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/0b/03dbeb8088e158b164a07a59a1009.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Weiner Group | [View](https://www.openjobs-ai.com/jobs/regional-sales-manager-white-city-ut-145063023738880794) |
| IT Applications Engineer V --	SAS, Python, R, Databricks, GitHub, SQL, SharePoint, PowerBI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/5d/0aac9b091e8a1c001ab78acce07fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente | [View](https://www.openjobs-ai.com/jobs/it-applications-engineer-v-sas-python-r-databricks-github-sql-sharepoint-powerbi-atlanta-ga-145063023738880795) |
| AVP, Programs Claims, North American Claims Group | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/8c/bbc797a0c9dda0499db3dfa89db9c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied World | [View](https://www.openjobs-ai.com/jobs/avp-programs-claims-north-american-claims-group-farmington-ct-145063023738880797) |

<p align="center">
  <em>...and 551 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated March 13, 2026
</p>
