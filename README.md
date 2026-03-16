<p align="center">
  <img src="https://img.shields.io/badge/jobs-429+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-341+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 341+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 187 |
| Management | 76 |
| Healthcare | 69 |
| Engineering | 48 |
| Sales | 23 |
| Finance | 8 |
| Operations | 8 |
| HR | 6 |
| Marketing | 4 |

**Top Hiring Companies:** Uncommon Schools, Varsity Tutors, a Nerdy Company, Detroit Medical Center, Jobot, Schindler Elevator Corporation (U.S.)

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
│  │ Sitemap     │   │ (429+ jobs) │   │ (README + HTML)     │   │
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
- **And 341+ other companies**

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
  <em>Updated March 16, 2026 · Showing 200 of 429+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Environmental Health Safety Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/a2/b7df2cdb4604fb70485206469fbb3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sensaria | [View](https://www.openjobs-ai.com/jobs/environmental-health-safety-specialist-scotts-valley-ca-146153513418752411) |
| Journeyman Plumber | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/f3/8cba54b99bdf43ec3f63e7d40f514.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Paschal Air, Plumbing & Electric | [View](https://www.openjobs-ai.com/jobs/journeyman-plumber-muskogee-ok-146153513418752412) |
| Manager, Digital Analytics - Amazon | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/ff/9bf245a3ba80329e687949118447b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Flamingo | [View](https://www.openjobs-ai.com/jobs/manager-digital-analytics-amazon-new-york-ny-146153513418752413) |
| Maintenance Generalist - A Shift- Portland, ME | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/7c/85930fb407cdc32b368b762c9ee3d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tyson Foods | [View](https://www.openjobs-ai.com/jobs/maintenance-generalist-a-shift-portland-me-portland-me-146153513418752414) |
| Composite Manufacturing Engineer II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/b5/ef84c73040faa82c2ae87a8fa9601.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Firefly Aerospace | [View](https://www.openjobs-ai.com/jobs/composite-manufacturing-engineer-ii-briggs-tx-146153513418752415) |
| Radiologic Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/70/790fb2794d9f929e9c5dbcd046cb7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PDI HEALTH (Preventive Diagnostics) | [View](https://www.openjobs-ai.com/jobs/radiologic-technologist-tampa-fl-146153513418752416) |
| Enterprise Provider Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/15/61712bef926d3b1c3071fbae577e9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vatica Health | [View](https://www.openjobs-ai.com/jobs/enterprise-provider-director-united-states-146153513418752417) |
| Manager, HR Compliance Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4b/0625f0a4b4aed1f2a977939481084.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Applied Materials | [View](https://www.openjobs-ai.com/jobs/manager-hr-compliance-manager-austin-tx-146153513418752418) |
| Tax Managing Director, Core Tax Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/0e/c4f94e12750f4805fb0664d062246.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BDO USA | [View](https://www.openjobs-ai.com/jobs/tax-managing-director-core-tax-services-nashville-tn-146153513418752419) |
| Tax Managing Director, Core Tax Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/0e/c4f94e12750f4805fb0664d062246.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BDO USA | [View](https://www.openjobs-ai.com/jobs/tax-managing-director-core-tax-services-gulfport-ms-146153513418752420) |
| Associate Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/38/86ceeb673708894af116aab6caf9f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> General Liability | [View](https://www.openjobs-ai.com/jobs/associate-attorney-general-liability-insurance-defense-tampa-fl-146153513418752421) |
| Solutions Sales Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/cf/bf22e187662dc7285fd5b797fbaee.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Reworld Waste | [View](https://www.openjobs-ai.com/jobs/solutions-sales-manager-home-ks-146153513418752424) |
| Territory Sales Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/a5/985996dbad62931750ab47fa67d51.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Laerdal Medical | [View](https://www.openjobs-ai.com/jobs/territory-sales-manager-syracuse-ny-146153513418752425) |
| Customer Service Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/f5/3ea2f6ad74217f69b763c9e4d9fe1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pride Health | [View](https://www.openjobs-ai.com/jobs/customer-service-representative-lees-summit-mo-146153513418752426) |
| Senior Data Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/0b/d528988d43e228f1ddc521d8dd10f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mastech Digital | [View](https://www.openjobs-ai.com/jobs/senior-data-engineer-new-york-united-states-146153513418752427) |
| Associate Creative Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/a5/4f566a7f0082077bf08f135b2f661.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Blue Hour Studios | [View](https://www.openjobs-ai.com/jobs/associate-creative-director-new-york-ny-146153513418752428) |
| Consumer Loan Administration | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/38/f7c69ff84f2d1429cab3fef891586.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arbor Bank | [View](https://www.openjobs-ai.com/jobs/consumer-loan-administration-omaha-ne-146153513418752429) |
| Clinical Research Nurse 250320 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/81/4dc9092df5346f6ad165de742e148.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Medix™ | [View](https://www.openjobs-ai.com/jobs/clinical-research-nurse-250320-lenexa-ks-146153513418752430) |
| Psychiatric Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/9b/0027af86cc54aaa92f323064fddcb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ambe Healthcare Staffing | [View](https://www.openjobs-ai.com/jobs/psychiatric-nurse-holyoke-ma-146153513418752431) |
| Nursing Student Summer Extern - Oral Surgery | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/c0/1c5ba9c7d1bf651c582c2f430da30.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Geisinger | [View](https://www.openjobs-ai.com/jobs/nursing-student-summer-extern-oral-surgery-danville-pa-146153513418752432) |
| CNA Certified Nursing Assistant (DAY SHIFT) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/91/4ce7df31b70acd793a58c60c7e15e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Masonicare | [View](https://www.openjobs-ai.com/jobs/cna-certified-nursing-assistant-day-shift-wallingford-ct-146153513418752433) |
| Physical Therapist Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/b6/3d29c799221843f27793a45df7486.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Green Oaks Physical Therapy | [View](https://www.openjobs-ai.com/jobs/physical-therapist-assistant-fort-worth-tx-146153513418752434) |
| Enterprise Account Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/enterprise-account-executive-lehi-ut-146153513418752435) |
| Software Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/db/e38c61911a78b4b76119a99f359e1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BeaconFire Inc. | [View](https://www.openjobs-ai.com/jobs/software-engineer-washington-united-states-146153513418752436) |
| Front of House Team Member - Connecticut Ave | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0c/60d748320d3ef571d73d459950446.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Call Your Mother | [View](https://www.openjobs-ai.com/jobs/front-of-house-team-member-connecticut-ave-washington-dc-146153513418752438) |
| System Integration And Test Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/dd/ef547cf8dbe8437bf952485357a17.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Applied Research Lab Penn S | [View](https://www.openjobs-ai.com/jobs/system-integration-and-test-engineer-state-college-pa-146153513418752439) |
| Director of Business Development | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/de/2cc5eb9d671bdf16729fdb8379323.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PCN | [View](https://www.openjobs-ai.com/jobs/director-of-business-development-austin-texas-metropolitan-area-146153513418752440) |
| Technical Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/55/d3486147c979be8d0bb9b9ff883db.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Galent | [View](https://www.openjobs-ai.com/jobs/technical-project-manager-berkeley-heights-nj-146153513418752441) |
| Senior MongoDB DBA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/01/b3620c3be49fbf4948033d9de9814.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EPAM Systems | [View](https://www.openjobs-ai.com/jobs/senior-mongodb-dba-georgia-146153513418752442) |
| Shift Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/e7/92c7d070681c63ba1c1fc0b6d8d8f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Selig Group | [View](https://www.openjobs-ai.com/jobs/shift-supervisor-forrest-il-146153513418752443) |
| Experienced Merchandiser Increase Your Earnings | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/46/5f3ae826f62983961f35a6a6bee48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jacent | [View](https://www.openjobs-ai.com/jobs/experienced-merchandiser-increase-your-earnings-la-puente-ca-146153513418752446) |
| Field Merchandiser Increase Your Earnings | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/46/5f3ae826f62983961f35a6a6bee48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jacent | [View](https://www.openjobs-ai.com/jobs/field-merchandiser-increase-your-earnings-butte-mt-146153513418752447) |
| Senior Procurement Analyst - Compliance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/14/ec3e84fadda11a5441caecb3afe24.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Leonardo DRS | [View](https://www.openjobs-ai.com/jobs/senior-procurement-analyst-compliance-danbury-ct-146153513418752448) |
| Pharmacy Administrative Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/c8/5453596183beb17c1cb28778cd173.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Houston Methodist | [View](https://www.openjobs-ai.com/jobs/pharmacy-administrative-specialist-sugar-land-tx-146153513418752449) |
| Assembly Operator 3 - 2nd shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/6b/2034d9cb32cbc1d3a4f0b9ef7ed9e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Southern States LLC | [View](https://www.openjobs-ai.com/jobs/assembly-operator-3-2nd-shift-hampton-ga-146153513418752450) |
| FP&A Analyst B4 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4b/0625f0a4b4aed1f2a977939481084.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> New College Grad (MBA | [View](https://www.openjobs-ai.com/jobs/fpa-analyst-b4-new-college-grad-mba-santa-clara-ca-santa-clara-ca-146153513418752451) |
| Tax Senior Manager, ASC740 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/0e/c4f94e12750f4805fb0664d062246.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BDO USA | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-asc740-nashville-tn-146153513418752452) |
| Senior Underwriter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/39/fc6fb50c435b5f4f06584523b2325.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arch Insurance Group Inc. | [View](https://www.openjobs-ai.com/jobs/senior-underwriter-greater-philadelphia-146153513418752453) |
| AWH Office Manager, part-time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/b2/65d11d783c2d2fe1c24affe479672.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ageless Men's Health | [View](https://www.openjobs-ai.com/jobs/awh-office-manager-part-time-ogden-ut-146153513418752454) |
| Claims Examiner, Commercial Auto | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/39/fc6fb50c435b5f4f06584523b2325.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Arch Insurance Group Inc. | [View](https://www.openjobs-ai.com/jobs/claims-examiner-commercial-auto-alpharetta-ga-146153513418752455) |
| Mold Maker | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/b5/46bed5a3d446aeb302c70d0ff58d6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Genuine Search Group | [View](https://www.openjobs-ai.com/jobs/mold-maker-st-paul-mn-146153513418752456) |
| AQX S113 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/07/18f202a2c3f6ec11dfeab418f5f27.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Program Analyst TMT Coordinator | [View](https://www.openjobs-ai.com/jobs/aqx-s113-program-analyst-tmt-coordinator-journeyman-secret-pentagon-city-va-146153513418752457) |
| Appian Architect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/61/6827db04debdb52286b1b5c31439d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Infosys | [View](https://www.openjobs-ai.com/jobs/appian-architect-dallas-tx-146153513418752458) |
| Experienced Automotive Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/13/ab374a204b4814a38fb8b6fcc6674.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wise Auto Group | [View](https://www.openjobs-ai.com/jobs/experienced-automotive-technician-vacaville-ca-146153513418752459) |
| Senior Structural Engineer \| Healthcare | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/d13445e635b696cfe83d2c7ce2c7e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DLR Group | [View](https://www.openjobs-ai.com/jobs/senior-structural-engineer-healthcare-sacramento-ca-146153513418752460) |
| Data Coordinator 1 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/2d/58ce1a20a4561c85d8ef7dcf60958.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Russell Tobin | [View](https://www.openjobs-ai.com/jobs/data-coordinator-1-bowling-green-ky-146153513418752461) |
| Police Officer (Full Time/Rotation) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/c0/1c5ba9c7d1bf651c582c2f430da30.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Geisinger | [View](https://www.openjobs-ai.com/jobs/police-officer-full-timerotation-scranton-pa-146153513418752462) |
| Electrical Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2b/cfaedc40d9f9a807b5ba6e69237ec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ellaway Blues Consulting | [View](https://www.openjobs-ai.com/jobs/electrical-engineer-dallas-fort-worth-metroplex-146153513418752463) |
| Physical Therapist Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/22/e2720ea72a9b5fed2c7657bf93747.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Carolina Physical Therapy and Sports Medicine | [View](https://www.openjobs-ai.com/jobs/physical-therapist-assistant-columbia-sc-146153513418752464) |
| Associate Attorney - General Civil Litigation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/associate-attorney-general-civil-litigation-raleigh-nc-146153513418752465) |
| IP Specialist - Hard Science | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/ip-specialist-hard-science-atlanta-ga-146153513418752466) |
| Business Development Manager, Cross-border MX | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/11/6753def23a7970f964fe5a364b43a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Total One Logistics Inc. | [View](https://www.openjobs-ai.com/jobs/business-development-manager-cross-border-mx-san-diego-ca-146153513418752467) |
| Production Supervisor (Nights) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/16/eb16fb3288b85652007be47c58c68.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> STERIS | [View](https://www.openjobs-ai.com/jobs/production-supervisor-nights-minneapolis-mn-146153513418752468) |
| Senior Specialist, Business Development- EPI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/4b/0e1ff0174ab71ef8823fc7cafe57d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Davis Polk & Wardwell LLP | [View](https://www.openjobs-ai.com/jobs/senior-specialist-business-development-epi-new-york-united-states-146153513418752469) |
| Referral Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/f7/1dd18d21a3bfa2f43c00266596d60.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Morgan & Morgan, P.A. | [View](https://www.openjobs-ai.com/jobs/referral-manager-united-states-146153513418752470) |
| Enterprise AI Solutions Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/16/5cecfce584c51e706af3e63fe0375.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TransPerfect | [View](https://www.openjobs-ai.com/jobs/enterprise-ai-solutions-consultant-boulder-co-146153513418752471) |
| Acute Care Physical Therapy Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/a1/cc07c18c32a98314938ae3d32333a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MedStar Health | [View](https://www.openjobs-ai.com/jobs/acute-care-physical-therapy-supervisor-district-of-columbia-united-states-146153513418752473) |
| Principal Medical Copywriter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/e8/d385cf8aefc6f12185e5be66ce0dc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cognite | [View](https://www.openjobs-ai.com/jobs/principal-medical-copywriter-united-states-146153513418752474) |
| Senior Claim Representative/Consultant - Construction Defect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/9f/333b6a1308a268c4f6a5cc7696fb1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Hartford | [View](https://www.openjobs-ai.com/jobs/senior-claim-representativeconsultant-construction-defect-united-states-146153513418752475) |
| Fair Hearings Agency Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/1d/9818d2dc2c9cf6517f03c60748904.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NYC Administration for Children's Services | [View](https://www.openjobs-ai.com/jobs/fair-hearings-agency-attorney-manhattan-ny-146153513418752476) |
| SAP Project Manager S/4HANA Public Cloud | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/bf/8d7f938355c95656472160bb91666.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 83zero | [View](https://www.openjobs-ai.com/jobs/sap-project-manager-s4hana-public-cloud-alabama-united-states-146153513418752477) |
| Part Time Merchandiser - Wichita, KS | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/bd/8724aab56f4b7e61d904e19e55eb5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American Greetings | [View](https://www.openjobs-ai.com/jobs/part-time-merchandiser-wichita-ks-wichita-ks-146153513418752478) |
| Research Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/02/da3d78241fe1ed39da349ee810b40.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MESO SCALE DIAGNOSTICS, LLC. | [View](https://www.openjobs-ai.com/jobs/research-associate-gaithersburg-md-146153513418752479) |
| Sr. Manager, Patient Marketing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/25/cae0ef6608d2a75f68aabd42af92b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Servier Pharmaceuticals | [View](https://www.openjobs-ai.com/jobs/sr-manager-patient-marketing-united-states-146153513418752481) |
| CNA Certified Nursing Assistant (EVENING SHIFT) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/91/4ce7df31b70acd793a58c60c7e15e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Masonicare | [View](https://www.openjobs-ai.com/jobs/cna-certified-nursing-assistant-evening-shift-wallingford-ct-146153513418752482) |
| Payroll Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7a/26aba643d7c627252411f88658e68.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IRIS Software Group | [View](https://www.openjobs-ai.com/jobs/payroll-specialist-illinois-united-states-146153513418752483) |
| Staff Nurse, RN - Day Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/3e/3c4fc8e8360113f72f29da1129a78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Banyan Treatment Centers | [View](https://www.openjobs-ai.com/jobs/staff-nurse-rn-day-shift-castle-rock-co-146153513418752484) |
| IP Specialist - Hard Science | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/ip-specialist-hard-science-new-york-ny-146153513418752485) |
| Recruiting Coordinator (Fixed Term) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/a9/0a942925e6511b525e9dc8ba45177.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 2U | [View](https://www.openjobs-ai.com/jobs/recruiting-coordinator-fixed-term-crystal-city-va-146153513418752486) |
| Registered Nurse (RN) - Family Practice | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/46/ef0e864744d60f5e6c7b587a4f9c4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Advocate Health Care | [View](https://www.openjobs-ai.com/jobs/registered-nurse-rn-family-practice-elgin-il-146153513418752487) |
| Oncology Nurse Care Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/46/ef0e864744d60f5e6c7b587a4f9c4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Advocate Health Care | [View](https://www.openjobs-ai.com/jobs/oncology-nurse-care-coordinator-crystal-lake-il-146153513418752488) |
| Sr Manufacturing Engineer (Welding exp. required) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/8c/ab4e83aabc2f76a8ababb1105984c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Schindler Elevator Corporation (U.S.) | [View](https://www.openjobs-ai.com/jobs/sr-manufacturing-engineer-welding-exp-required-clinton-nc-146153513418752489) |
| Sales Support Intern - Summer 2026 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/8c/ab4e83aabc2f76a8ababb1105984c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Schindler Elevator Corporation (U.S.) | [View](https://www.openjobs-ai.com/jobs/sales-support-intern-summer-2026-raleigh-nc-146153513418752490) |
| Territory Portfolio Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/8c/ab4e83aabc2f76a8ababb1105984c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Schindler Elevator Corporation (U.S.) | [View](https://www.openjobs-ai.com/jobs/territory-portfolio-manager-dallas-tx-146153513418752491) |
| Industrial Safety Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/c5/e694bf3d27347edce19594504bce9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Interlake Mecalux, Inc. | [View](https://www.openjobs-ai.com/jobs/industrial-safety-engineer-melrose-park-il-146153513418752493) |
| Lighting Showroom Sales | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/2a/eb5053fb6d0744839fbcbe9bf428a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rexel USA | [View](https://www.openjobs-ai.com/jobs/lighting-showroom-sales-pelham-al-146153513418752494) |
| Environmental Services Aide | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/84/1ce1f9f705011571e310dd0e69d9f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UR Thompson Health | [View](https://www.openjobs-ai.com/jobs/environmental-services-aide-canandaigua-ny-146153513418752495) |
| Payments Systems Specialist – ACH | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/27/f9afa46b167f70a5df245aa18f2db.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EECU | [View](https://www.openjobs-ai.com/jobs/payments-systems-specialist-ach-fort-worth-tx-146153513418752496) |
| Phlebotomist I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/b6/024ac3e2a930ca3de64b939488e62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Quest Diagnostics | [View](https://www.openjobs-ai.com/jobs/phlebotomist-i-sterling-heights-mi-146153513418752497) |
| ASST HEAD FACILITY SVPER-ELEM/MID/EX/CTR | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/c5/428c26994165889fb3d063d8079e7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Broward County Public Schools | [View](https://www.openjobs-ai.com/jobs/asst-head-facility-svper-elemmidexctr-fort-lauderdale-fl-146153513418752498) |
| Outreach Liaison - Indianapolis | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/b4/e0f1f97a2a4376685907340bfabf1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Author Health | [View](https://www.openjobs-ai.com/jobs/outreach-liaison-indianapolis-united-states-146153513418752499) |
| Senior Operations Manager- Ocean Marine | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/9f/333b6a1308a268c4f6a5cc7696fb1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Hartford | [View](https://www.openjobs-ai.com/jobs/senior-operations-manager-ocean-marine-danbury-ct-146153513418752500) |
| Financial Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/59/222c52c2d9a97b76ecb73821c35ea.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MATCOR Metal Fabrication | [View](https://www.openjobs-ai.com/jobs/financial-analyst-lexington-nc-146153513418752501) |
| POLITICO Live Events Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/73/fe9e2c2a2f7bf602fd223c0613f45.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> POLITICO | [View](https://www.openjobs-ai.com/jobs/politico-live-events-specialist-arlington-va-146153513418752502) |
| Medical Social Worker | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/5c/eca0abc4106509e2cf1cc34c74065.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Johns Hopkins Howard County Medical Center | [View](https://www.openjobs-ai.com/jobs/medical-social-worker-columbia-md-146153513418752503) |
| Sr Financial Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/5c/eca0abc4106509e2cf1cc34c74065.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Johns Hopkins Howard County Medical Center | [View](https://www.openjobs-ai.com/jobs/sr-financial-analyst-columbia-md-146153513418752504) |
| Sales Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/2e/58c1838ce47d8d30fc10125a99fa1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Konica Minolta Business Solutions U.S.A., Inc. | [View](https://www.openjobs-ai.com/jobs/sales-executive-peoria-il-146153513418752505) |
| Cook | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/d5/495c8eeea0a014d17608cd4bff05e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> FREEDOM POINTE AT THE VILLAGES, LLC | [View](https://www.openjobs-ai.com/jobs/cook-the-villages-fl-146153513418752506) |
| Pediatric Clinical Respiratory Specialist - Stork Team | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/1f/82e49bae801110e99bcd57841853d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Indiana University Health | [View](https://www.openjobs-ai.com/jobs/pediatric-clinical-respiratory-specialist-stork-team-indianapolis-in-146153513418752507) |
| Activities Coordinator-Memory Care | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/91/ba3790fe06726cf8da9cd9969db32.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Benchmark Senior Living | [View](https://www.openjobs-ai.com/jobs/activities-coordinator-memory-care-white-river-junction-vt-146153513418752509) |
| Inventory Maintenance Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b1/56eebf98c2eb1d71ee8e008152cb1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pacific Seafood | [View](https://www.openjobs-ai.com/jobs/inventory-maintenance-intern-newport-or-146153513418752510) |
| Truck Driver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/98/17ac940bbf2ec56c4534762772759.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ryerson | [View](https://www.openjobs-ai.com/jobs/truck-driver-lavonia-ga-146153513418752511) |
| Principal Embedded Firmware Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/80/b935baffc8aabebbc4987e4d293f3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Synchron | [View](https://www.openjobs-ai.com/jobs/principal-embedded-firmware-engineer-brooklyn-ny-146153513418752512) |
| Release Train Engineer (RTE) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/c1/2bb1e118f3f92fc715db93b747e65.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> COUNTRY Financial® | [View](https://www.openjobs-ai.com/jobs/release-train-engineer-rte-bloomington-il-146153513418752513) |
| Field Service Engineer I - Charlotte, NC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/ad/4fd0f970de5649010b465775dba85.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Olympus Corporation | [View](https://www.openjobs-ai.com/jobs/field-service-engineer-i-charlotte-nc-center-valley-pa-146153513418752514) |
| Banking Enterprise Risk & Regulatory Reporting SME | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/e7/9ce6ff8b0bc9ba6dd507163022fec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Upwork | [View](https://www.openjobs-ai.com/jobs/banking-enterprise-risk-regulatory-reporting-sme-florida-city-fl-146153513418752515) |
| Territory Vice President | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/8c/ab4e83aabc2f76a8ababb1105984c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Schindler Elevator Corporation (U.S.) | [View](https://www.openjobs-ai.com/jobs/territory-vice-president-philadelphia-pa-146153513418752516) |
| Sales Rep - Service | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/8c/ab4e83aabc2f76a8ababb1105984c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Schindler Elevator Corporation (U.S.) | [View](https://www.openjobs-ai.com/jobs/sales-rep-service-los-angeles-ca-146153513418752517) |
| 1st Grade Bilingual (Spanish) Teacher - Pleasant Acres 2026/27 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/2f/c1cdd551554bcc712459fa55bf23f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rantoul City School Dst 137 | [View](https://www.openjobs-ai.com/jobs/1st-grade-bilingual-spanish-teacher-pleasant-acres-202627-rantoul-il-146153513418752519) |
| Area Sales Manager - Lancaster/Harrisburg On-Premise | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/f7/8b06b071980066667613e0f57d0ef.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stateside Brands | [View](https://www.openjobs-ai.com/jobs/area-sales-manager-lancasterharrisburg-on-premise-lancaster-pa-146153513418752520) |
| Career Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/d2/6f9946731ef25d617b5c89b17abc0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Equus Workforce Solutions | [View](https://www.openjobs-ai.com/jobs/career-advisor-racine-wi-146153513418752521) |
| Transportation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/b8/dd2500be2df4a673954af1fb4958f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Spirit AeroSystems | [View](https://www.openjobs-ai.com/jobs/transportation-wichita-ks-146153513418752522) |
| 2nd Shift Senior Maintenance Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/28/77715dcb8375ddcd2b537394eb5b1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Asurion | [View](https://www.openjobs-ai.com/jobs/2nd-shift-senior-maintenance-technician-smyrna-tn-146153513418752523) |
| Long Haul Deployment Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/39/29163ecf1e3a39096f1f0ea18fde3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Zayo Group | [View](https://www.openjobs-ai.com/jobs/long-haul-deployment-project-manager-missouri-united-states-146153513418752524) |
| Production Operator II - Wash Line/Inventory | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/d9/e81e7066050020803a10b978208ba.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CoorsTek, Inc. | [View](https://www.openjobs-ai.com/jobs/production-operator-ii-wash-lineinventory-golden-co-146153513418752525) |
| Warehouse Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/c5/2dddcad8a77d4b63baabc0c09ab63.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Red River Commodities Inc | [View](https://www.openjobs-ai.com/jobs/warehouse-associate-fargo-nd-146153513418752526) |
| Techno-functional ETRM/CTRM Business Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/27/c8e7d0bf98d55a76384dd6357a0f6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Search Services | [View](https://www.openjobs-ai.com/jobs/techno-functional-etrmctrm-business-analyst-houston-tx-146153513418752527) |
| Licensed Practical Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/5c/936055411383231107098c09dc285.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sono Bello | [View](https://www.openjobs-ai.com/jobs/licensed-practical-nurse-edina-mn-146153513418752528) |
| Buyer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/366ba963b46f9ae77e05b60fe4f49.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gates Corporation | [View](https://www.openjobs-ai.com/jobs/buyer-siloam-springs-ar-146153513418752529) |
| AI and Distributed Systems Fullstack Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Senior Manager | [View](https://www.openjobs-ai.com/jobs/ai-and-distributed-systems-fullstack-engineer-senior-manager-consulting-location-open-milwaukee-wi-146153513418752530) |
| STNA Night Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/53/093552b8e21b023d93780375f06cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Friendship Village Of Dublin | [View](https://www.openjobs-ai.com/jobs/stna-night-shift-dublin-oh-146153513418752531) |
| Desktop Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/96/1e0701f361b54d26ffe840960a69b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dexian | [View](https://www.openjobs-ai.com/jobs/desktop-technician-colorado-springs-co-146153513418752532) |
| Supervisor, QC Data Review Release Testing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/96/ad41d00f7cbd066d7ef38e2520bbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cardinal Health | [View](https://www.openjobs-ai.com/jobs/supervisor-qc-data-review-release-testing-indianapolis-in-146153513418752533) |
| Head of AI Visibility | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/d2/9a56f9546d28e8640a2953adc360e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brainlabs | [View](https://www.openjobs-ai.com/jobs/head-of-ai-visibility-san-francisco-bay-area-146153513418752534) |
| Travel Commodity Manager (Global Procurement & Travel Operations) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/9e/6327424362112bd43162f2a1a0643.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Coherent Corp. | [View](https://www.openjobs-ai.com/jobs/travel-commodity-manager-global-procurement-travel-operations-santa-clara-ca-146153513418752535) |
| Workers Compensation Claims Representative \| Pasadena, CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/fb/e74f467c92d9ea99f531cff72aadb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sedgwick | [View](https://www.openjobs-ai.com/jobs/workers-compensation-claims-representative-pasadena-ca-pasadena-ca-146153513418752536) |
| Chief, Division of Breast Medical Oncology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/4f/ea93079e0a8e0f39e6da66e8ad4fb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AMN Healthcare Leadership Solutions | [View](https://www.openjobs-ai.com/jobs/chief-division-of-breast-medical-oncology-philadelphia-pa-146153513418752537) |
| Founding Engineering Manager - New York | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/69/3d5a20613a03935caf66fc4345a7a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Giga | [View](https://www.openjobs-ai.com/jobs/founding-engineering-manager-new-york-new-york-ny-146153513418752538) |
| Classroom Assistant Teacher - Spring, Wisconsin ($15.75/HR) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/1a/68f14dc0e097d37b3eae320b0f667.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UMOS, Inc. | [View](https://www.openjobs-ai.com/jobs/classroom-assistant-teacher-spring-wisconsin-1575hr-wautoma-wi-146153513418752539) |
| Foodservice Worker | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/da/658fd81b2cf5c72e80cfdbe96ad40.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SFE- Southwest Foodservice Excellence | [View](https://www.openjobs-ai.com/jobs/foodservice-worker-clinton-wi-146153513418752540) |
| Head of US Marketing, Diagnosis | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/8e/09352826ddcffddd04f2b791a410a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insmed Incorporated | [View](https://www.openjobs-ai.com/jobs/head-of-us-marketing-diagnosis-headquarters-nj-146153513418752541) |
| Application Development and Implementation Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/e8/34f1ec90499978bc052c2d1060689.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Siemens Healthineers | [View](https://www.openjobs-ai.com/jobs/application-development-and-implementation-analyst-malvern-pa-146153513418752542) |
| Payroll Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/4c/dddb24bcc913c648702c81835897a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Advanced Correctional Healthcare, Inc. | [View](https://www.openjobs-ai.com/jobs/payroll-clerk-franklin-tn-146153513418752543) |
| Senior IT Systems Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/4a/9e7f41b7c7c36471e6f778af729f4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Central States | [View](https://www.openjobs-ai.com/jobs/senior-it-systems-engineer-tontitown-ar-146153513418752544) |
| Patient Access Associate (FT; Days) - Crescent City Physician's Inc (LSU OBGyn & Peds) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/f9/bfffb3e66e29ed5ede3a06418e697.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LCMC Health | [View](https://www.openjobs-ai.com/jobs/patient-access-associate-ft-days-crescent-city-physicians-inc-lsu-obgyn-peds-new-orleans-la-146153513418752545) |
| Supervisor, Histology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/46/ffb9b3425681f82aec297216b5d0a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Memorial Sloan Kettering Cancer Center | [View](https://www.openjobs-ai.com/jobs/supervisor-histology-new-york-ny-146153513418752546) |
| Project Manager (FT) Facilities Design Construction | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a4/ebab54a580dbfc71fdd4c5b098ecb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Huntsville Hospital | [View](https://www.openjobs-ai.com/jobs/project-manager-ft-facilities-design-construction-huntsville-al-146153513418752547) |
| Maintenance Associate - 12 hr Nights | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/cf/4441791f915d9d8f28fb3b08acae0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Avient Corporation | [View](https://www.openjobs-ai.com/jobs/maintenance-associate-12-hr-nights-birmingham-al-146153513418752548) |
| Human Resources Business Partner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/2d/d5deb38d3fbd8533f530a55e73d51.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mactac North America | [View](https://www.openjobs-ai.com/jobs/human-resources-business-partner-minneapolis-mn-146153513418752549) |
| Dental Hygienist-$5,000 Sign on Bonus! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/40/c17640a8752eac18370aeff611f63.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Imagen Dental Partners | [View](https://www.openjobs-ai.com/jobs/dental-hygienist-5000-sign-on-bonus-hastings-mn-146153513418752550) |
| Manager, Major Gifts | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/b5/ee72dd3ad45fd1c5959433f5c41df.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> United Way of New York City | [View](https://www.openjobs-ai.com/jobs/manager-major-gifts-new-york-ny-146153513418752551) |
| Sr. Warehouse Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/fa/d1cdd908af9b4f4285e530e6c0854.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TAS Energy | [View](https://www.openjobs-ai.com/jobs/sr-warehouse-associate-greater-houston-146153513418752552) |
| Customer Service Rep(07369) 1595 2nd Ave Ne | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/c3/db8b53ac9db0fb462a49a5c694d42.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Domino's | [View](https://www.openjobs-ai.com/jobs/customer-service-rep07369-1595-2nd-ave-ne-cambridge-mn-146153513418752553) |
| Staff Technical Recruiter, General Engineering | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/aa/225e7e387c8ac922a9cf88e3b2c7a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Robinhood | [View](https://www.openjobs-ai.com/jobs/staff-technical-recruiter-general-engineering-menlo-park-ca-146153513418752554) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/72/124fe9ddc1e9e1ed6ff1fd627a004.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CoxHealth | [View](https://www.openjobs-ai.com/jobs/registered-nurse-branson-mo-146153513418752555) |
| Appraisal Desk Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/42/cbe635daea625842686d76e001d60.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Premier Mortgage Associates | [View](https://www.openjobs-ai.com/jobs/appraisal-desk-coordinator-united-states-146153513418752556) |
| Energy Resource Adoption Forecasting Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/6d/985c9408072c3396c4604c932db68.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DNV | [View](https://www.openjobs-ai.com/jobs/energy-resource-adoption-forecasting-consultant-columbus-oh-146153513418752557) |
| CNA - Geriatric Psych | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fb/881bf3e57eb8b3449a49aacbd9a48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MultiCare Health System | [View](https://www.openjobs-ai.com/jobs/cna-geriatric-psych-auburn-wa-146153513418752558) |
| Scientist, Protein Engineering | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/02/da3d78241fe1ed39da349ee810b40.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MESO SCALE DIAGNOSTICS, LLC. | [View](https://www.openjobs-ai.com/jobs/scientist-protein-engineering-gaithersburg-md-146153513418752559) |
| CNA Certified Nursing Assistant (NIGHT SHIFT) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/91/4ce7df31b70acd793a58c60c7e15e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Masonicare | [View](https://www.openjobs-ai.com/jobs/cna-certified-nursing-assistant-night-shift-wallingford-ct-146153513418752560) |
| Senior Recruiter: Emerging Talent & Global Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/59/e008b4891395fc399b1a647a0a10d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CarGurus | [View](https://www.openjobs-ai.com/jobs/senior-recruiter-emerging-talent-global-operations-boston-ma-146153513418752561) |
| Tax Preparer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/tax-preparer-wheaton-il-146153513418752562) |
| Senior DevSecOps Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/6d/c987f9b9408e47db2e2a1f53e094c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Steampunk, Inc. | [View](https://www.openjobs-ai.com/jobs/senior-devsecops-engineer-mclean-va-146153513418752563) |
| Truck Driver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/e6/25b381c02802eb17151f0994a635a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City Harvest | [View](https://www.openjobs-ai.com/jobs/truck-driver-brooklyn-ny-146153513418752564) |
| Quality Assumptions Processor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/b3/3014d92141e92affc4ffd44f6d961.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PENNYMAC | [View](https://www.openjobs-ai.com/jobs/quality-assumptions-processor-moorpark-ca-146153513418752565) |
| Systems Test Engineer - Zero Trust Client | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/32/d84622a5ed88e40d37a784e4e985f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cloudflare | [View](https://www.openjobs-ai.com/jobs/systems-test-engineer-zero-trust-client-austin-tx-146153513418752566) |
| Solution Consultant - HCM | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/10/1dd90148f719d288dd6f13ac4e84e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Workday | [View](https://www.openjobs-ai.com/jobs/solution-consultant-hcm-delaware-united-states-146153513418752567) |
| Regional Sales Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/10/1dd90148f719d288dd6f13ac4e84e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Workday | [View](https://www.openjobs-ai.com/jobs/regional-sales-director-boston-ma-146153513418752568) |
| Payroll Opportunities - Entry Level | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7a/26aba643d7c627252411f88658e68.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IRIS Software Group | [View](https://www.openjobs-ai.com/jobs/payroll-opportunities-entry-level-ann-arbor-mi-146153513418752569) |
| Corporate Counsel | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/ac/b757dc024c0d87cca65e4953b75ae.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Battery Network | [View](https://www.openjobs-ai.com/jobs/corporate-counsel-united-states-146153513418752570) |
| Phlebotomist III Site Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/b6/024ac3e2a930ca3de64b939488e62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Quest Diagnostics | [View](https://www.openjobs-ai.com/jobs/phlebotomist-iii-site-lead-cumming-ga-146153513418752571) |
| Kawasaki Robot Programmer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/105e0c7057f595d2ab61fdf3f9bb6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gabletek Robotics and Controls Solutions | [View](https://www.openjobs-ai.com/jobs/kawasaki-robot-programmer-troy-mi-146153513418752572) |
| Patient Access Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/0c/206f341858042722f3ec0ac098a5a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cone Health | [View](https://www.openjobs-ai.com/jobs/patient-access-specialist-greensboro-nc-146153513418752573) |
| CASE MANAGER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/53/79adbec72478aadb0425d828d13a7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of Louisiana | [View](https://www.openjobs-ai.com/jobs/case-manager-baton-rouge-la-146153513418752574) |
| CNA / Home Health Aide/ PCA / Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/1a/3106890d0299e707d3a70203e4fb2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dentserv Dental Services | [View](https://www.openjobs-ai.com/jobs/cna-home-health-aide-pca-assistant-farmingdale-ny-146153513418752575) |
| Sr. HR Business Partner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/60/030a3e716b0174be846e344163fa9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Horizon Blue Cross Blue Shield of New Jersey | [View](https://www.openjobs-ai.com/jobs/sr-hr-business-partner-newark-nj-146153513418752576) |
| AI/Machine Learning Data Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/a3/6439f6138546cc12eff1e077fb510.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Acosta Group | [View](https://www.openjobs-ai.com/jobs/aimachine-learning-data-engineer-jacksonville-fl-146153513418752577) |
| PMR Therapy Aide (Full-Time, Day Shift) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/22/09e99b3082b3fd5395bf331ebd02b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Penn Medicine Lancaster General Health | [View](https://www.openjobs-ai.com/jobs/pmr-therapy-aide-full-time-day-shift-lancaster-pa-146153513418752578) |
| Patient Care Assistant-7F General Medical (.6FTE, Evenings) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/22/09e99b3082b3fd5395bf331ebd02b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Penn Medicine Lancaster General Health | [View](https://www.openjobs-ai.com/jobs/patient-care-assistant-7f-general-medical-6fte-evenings-lancaster-pa-146153513418752579) |
| Assembly Specialist 3 - 1st shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/6b/2034d9cb32cbc1d3a4f0b9ef7ed9e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Southern States LLC | [View](https://www.openjobs-ai.com/jobs/assembly-specialist-3-1st-shift-hampton-ga-146153513418752580) |
| Sales Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/e9/6f899d663190ef9827d2e9c3389b7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SMS group USA | [View](https://www.openjobs-ai.com/jobs/sales-engineer-pittsburgh-pa-146153513418752581) |
| Group Product Manager - B2B API Platform (Remote) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/22/e5613aae801fc0584470e0bfac5f7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Progressive Leasing | [View](https://www.openjobs-ai.com/jobs/group-product-manager-b2b-api-platform-remote-arizona-united-states-146153513418752582) |
| Effect of Wildfires on Ocean Biogeochemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e9/794c633a19eccdee42dce0391bdf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ORAU | [View](https://www.openjobs-ai.com/jobs/effect-of-wildfires-on-ocean-biogeochemistry-greenbelt-md-146153513418752583) |
| Senior Registered Private Client Associate - Garden City, NY | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/59/75423a32e55cce2e4c3300e757640.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Janney Montgomery Scott LLC | [View](https://www.openjobs-ai.com/jobs/senior-registered-private-client-associate-garden-city-ny-garden-city-ny-146153513418752584) |
| Clinical Research Coordinator II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/1b/15e47d851b9980ed5ecd5420fe557.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Velocity Clinical Research, Inc. | [View](https://www.openjobs-ai.com/jobs/clinical-research-coordinator-ii-gaffney-sc-146153513418752585) |
| Senior AI Solutions Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/07/06f23654c4ad6e9e9590e400195c4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OneStream Software | [View](https://www.openjobs-ai.com/jobs/senior-ai-solutions-specialist-united-states-146153513418752586) |
| Basic EMT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2d/26cff459c87747e97b89063056514.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trinity Health MI | [View](https://www.openjobs-ai.com/jobs/basic-emt-muskegon-mi-146153513418752587) |
| Semi Mfg Technician 2 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/c2/3a8bf29a191f18aee814737e2a6ec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Nokia | [View](https://www.openjobs-ai.com/jobs/semi-mfg-technician-2-sunnyvale-ca-146153513418752588) |
| Quality Assurance Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/1a/8506a3be3fc2f17c517e4725d2b7a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PS Seasoning | [View](https://www.openjobs-ai.com/jobs/quality-assurance-manager-iron-ridge-wi-146153513418752589) |
| Center Manager/Child Dev. Coordinator - Plainfield, Wisconsin | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/1a/68f14dc0e097d37b3eae320b0f667.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UMOS, Inc. | [View](https://www.openjobs-ai.com/jobs/center-managerchild-dev-coordinator-plainfield-wisconsin-plainfield-wi-146153513418752590) |
| Supv Patient Access | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/08/5a80dffd24e569e0406a10aaff7da.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Palomar Health | [View](https://www.openjobs-ai.com/jobs/supv-patient-access-poway-ca-146153513418752591) |
| Client Service Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/06/5c21ed4050a4f6fdf241e66f38564.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Clark Schaefer Hackett | [View](https://www.openjobs-ai.com/jobs/client-service-specialist-cincinnati-oh-146153513418752592) |
| Infection Preventionist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/f9/bfffb3e66e29ed5ede3a06418e697.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LCMC Health | [View](https://www.openjobs-ai.com/jobs/infection-preventionist-new-orleans-la-146153513418752593) |
| LPN - Pain Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/1f/82e49bae801110e99bcd57841853d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Indiana University Health | [View](https://www.openjobs-ai.com/jobs/lpn-pain-management-muncie-in-146153513418752594) |
| Human Resources Business Partner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/b8/3130b6dfd100a4f6a9897dd41a374.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Music & Arts | [View](https://www.openjobs-ai.com/jobs/human-resources-business-partner-frederick-md-146153513418752595) |
| Dental Hygienist (RDH) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/19/4465a98cb0783f45f5a2800940376.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aspen Dental | [View](https://www.openjobs-ai.com/jobs/dental-hygienist-rdh-cincinnati-oh-146153513418752596) |
| General Dentists | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ae/f2c0bba4c170a9f498e708c2a9e74.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dentrust Optimized Care Solutions | [View](https://www.openjobs-ai.com/jobs/general-dentists-providence-ri-146153513418752597) |
| Aerial Foreman (CDL Required) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/0b/203d3ea402d4561448215f578de2a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MasTec Communications Group | [View](https://www.openjobs-ai.com/jobs/aerial-foreman-cdl-required-lewisville-tx-146153513418752598) |
| Travel Tower Foreman | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/0b/203d3ea402d4561448215f578de2a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MasTec Communications Group | [View](https://www.openjobs-ai.com/jobs/travel-tower-foreman-united-states-146153513418752599) |
| Field Service Engineer - Jefferson City, MO | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/1f/e875d8bf7e3a024efcd248690044c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NCR Voyix | [View](https://www.openjobs-ai.com/jobs/field-service-engineer-jefferson-city-mo-jefferson-city-mo-146153513418752600) |
| Director of Student Housing Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/94/64543940cae538c8f5aa93dc88177.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> COCM | [View](https://www.openjobs-ai.com/jobs/director-of-student-housing-operations-pittsburgh-pa-146153513418752601) |
| Associate Infrastructure Engineer - 2024188 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/37/c877a660b21a4133a002fba26e9dc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Software Engineering Institute | [View](https://www.openjobs-ai.com/jobs/associate-infrastructure-engineer-2024188-pittsburgh-pa-146153513418752602) |
| Respiratory Therapist-Full Time Nights Sign on bonus eligible | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/4f/3704903ccbd6ba362787d4bde3c66.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northwestern Medicine | [View](https://www.openjobs-ai.com/jobs/respiratory-therapist-full-time-nights-sign-on-bonus-eligible-mchenry-il-146153513418752603) |
| Test Technician (GL6) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/59/2c838ae6da3f11ec9dfcfcdde8bf6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Foxconn Industrial Internet USA | [View](https://www.openjobs-ai.com/jobs/test-technician-gl6-mount-pleasant-wi-146153513418752604) |
| Principal Law Clerk | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/a3/28f2e8a5c1c3e8e977432c83ae1ef.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> New York State Unified Court System | [View](https://www.openjobs-ai.com/jobs/principal-law-clerk-new-york-city-metropolitan-area-146153513418752605) |
| Veterinary Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7b/309e78447acaf7f5bdd8cc56f4b23.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NVA General Practice | [View](https://www.openjobs-ai.com/jobs/veterinary-assistant-moss-bluff-la-146153513418752606) |
| CLIN NURSE III | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/b4/ef38cfcf3bde4fe4c5376fb9d518f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Covenant Health | [View](https://www.openjobs-ai.com/jobs/clin-nurse-iii-lane-county-or-146153513418752607) |
| Imaging Manager - Off Campus ED | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fb/881bf3e57eb8b3449a49aacbd9a48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MultiCare Health System | [View](https://www.openjobs-ai.com/jobs/imaging-manager-off-campus-ed-bonney-lake-wa-146153513418752608) |
| Security Officer I (Full-Time/Evenings) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/c0/1c5ba9c7d1bf651c582c2f430da30.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Geisinger | [View](https://www.openjobs-ai.com/jobs/security-officer-i-full-timeevenings-scranton-pa-146153513418752609) |
| National Accounts Representative - Central Market | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/52/5cead2bc610a2782236e217c328df.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Benjamin Moore | [View](https://www.openjobs-ai.com/jobs/national-accounts-representative-central-market-carol-stream-il-146153513418752610) |
| Operations Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/98/17ac940bbf2ec56c4534762772759.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ryerson | [View](https://www.openjobs-ai.com/jobs/operations-supervisor-jackson-ms-146153513418752611) |
| Inside Sales Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/16/ec0ad37d00bfe9519b40d47b61fca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> S&G Carpet and More | [View](https://www.openjobs-ai.com/jobs/inside-sales-associate-rocklin-ca-146153513418752612) |
| High School History Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/51/69bf73bfdc61c534401739e9d691a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Uncommon Schools | [View](https://www.openjobs-ai.com/jobs/high-school-history-teacher-boston-ma-146154494885888000) |
| Sr. Plant Electrician/Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/6a/1557e8f43b63ea21c9344e0e4c432.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TenCate Protective Fabrics | [View](https://www.openjobs-ai.com/jobs/sr-plant-electricianmechanic-senoia-ga-146154494885888001) |
| Board Certified Behavior Analyst (BCBA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/b2/2432ee454ee39e17cd6b0865b2b3e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Action Behavior Centers | [View](https://www.openjobs-ai.com/jobs/board-certified-behavior-analyst-bcba-tucson-az-146154494885888002) |
| Hairstylist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/2d/86c7c907ba37d2df500018efb45a0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Poarch Creek Indians | [View](https://www.openjobs-ai.com/jobs/hairstylist-roseville-mn-146154494885888003) |
| Jump Start Rad Tech | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/fd/87e099ca4630b42393bb3f9f936c9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trinity Health | [View](https://www.openjobs-ai.com/jobs/jump-start-rad-tech-des-moines-ia-146154494885888004) |
| Registered Behavior Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/b2/2432ee454ee39e17cd6b0865b2b3e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Action Behavior Centers | [View](https://www.openjobs-ai.com/jobs/registered-behavior-technician-horsham-pa-146154494885888005) |
| Loan Officer - Rogers Main | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/56/0154fad2443173ec911f939152ad6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> First Western | [View](https://www.openjobs-ai.com/jobs/loan-officer-rogers-main-rogers-ar-146154494885888007) |
| Senior Project Manager - Federal Program | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/d9/5ed8c1e93b47def4e766bdb9cb4ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stantec | [View](https://www.openjobs-ai.com/jobs/senior-project-manager-federal-program-virginia-beach-va-146154494885888009) |

<p align="center">
  <em>...and 229 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated March 16, 2026
</p>
