

### Overview
A custom-built core system supporting order processing, sales, accounting, and inter-department workflows. Originally developed in-house to accommodate complex logistics and approval rules that were difficult to model in standard ERP products such as SAP.

The system has evolved over 20+ years and is heavily integrated with external applications through APIs and nightly batch processes.

### Vision
To maintain operational stability while enabling modernization through modularity, observability, and reduced vendor lock-in.

### Target Users
- Sales, procurement, and accounting departments using daily transactions
- Internal IT teams and external SI partners responsible for maintenance
- Business analysts depending on master data and process outputs

### User Problems
- Long-standing system with no clear subsystem boundaries
- Business logic is mixed into shared components, making changes risky
- Operational teams rely on CSV + Excel-based tools (Shadow IT) to compensate
- Difficult to onboard new developers or pass on system knowledge

### Key Features
- Nightly batch processing for financial closing and inventory
- API-based integration with surrounding SoE systems (high call volume during daytime)
- Centralized master data handling (e.g., item, vendor, customer)

### Constraints
- Java-based system with monolithic structure; no FE/BE separation
- Oracle database nearing connection capacity during peak times
- Shared logic is deeply entangled with core workflows
- Some business rules (e.g., inventory adjustment logic, approval sequences) are deeply embedded in the code and were not compatible with standard ERP workflows
- Attempts to migrate parts of the system to SAP were made in the past, but operational mismatches (especially in logistics) caused the plan to be shelved
- Maintenance is outsourced and highly specialized; modification risk is high

### Known Unknowns
- How to remap business logic currently embedded in shared utilities
- Data migration complexity across operational and historical datasets
- Whether breaking apart batch processes is viable without major downtime
- To what extent could business processes be adapted to fit a modern ERP like SAP?
- Would operational teams accept changes required for ERP-standard workflows?

### Why Now?
- The system is approaching architectural and operational limits (DB, performance, staffing)
- SI partners are unable to secure skilled engineers for legacy stack
- Increasing need for API-based integration and SaaS adoption across departments