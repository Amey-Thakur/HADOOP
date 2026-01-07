<div align="center">

  <a name="readme-top"></a>
  # HADOOP - Matrix Multiplication

  [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Completed-success)
  [![Technology](https://img.shields.io/badge/Technology-Python%203-orange)](https://github.com/Amey-Thakur/HADOOP)
  [![Developed by Amey Thakur](https://img.shields.io/badge/Developed%20by-Amey-Thakur-blue)](https://github.com/Amey-Thakur)

  An implementation of Matrix Multiplication using the MapReduce paradigm in Python, designed for parallel processing in distributed environments and Big Data Analytics.

  **[Source Code](Source%20Code/)** &nbsp;·&nbsp; **[Technical Specification](docs/SPECIFICATION.md)** &nbsp;·&nbsp; **[Google Colaboratory](Source%20Code/HADOOP.ipynb)**

</div>

---

<div align="center">

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#mapreduce-process-flow) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

</div>

---

<!-- AUTHORS -->
<div align="center">

  <a name="authors"></a>
  ## Authors

  **Terna Engineering College | Computer Engineering | Batch of 2022**

  <table>
  <tr>
  <td align="center">
  <a href="https://github.com/Amey-Thakur">
  <img src="https://github.com/Amey-Thakur.png" width="180px;" alt="Amey Thakur"/><br />
  <sub><b>Amey Thakur</b></sub>
  </a><br /><br />
  <a href="https://orcid.org/0000-0001-5644-1575">
  <img src="https://img.shields.io/badge/ORCID-0000--0001--5644--1575-brightgreen" alt="ORCID"/>
  </a>
  </td>
  </tr>
  </table>

</div>

---

<!-- OVERVIEW -->
<a name="overview"></a>
## Overview

**HADOOP** represents a pivotal milestone in the study of the **MapReduce Paradigm**. Developed during the academic study of Big Data Analytics, this project focuses on the practical application of parallel processing to execute large-scale matrix multiplication across distributed environments.

The project utilizes Python 3 to simulate the partitioning and aggregation of data, leveraging a coordinate-based key-value system to ensure computational accuracy and efficiency in a distributed architecture.

> [!TIP]
> **Hadoop Streaming Integration**
>
> This implementation is designed for compatibility with Hadoop Streaming, utilizing standard UNIX pipes (stdin/stdout). The Mapper partitions Matrix A and B elements into intermediate cell-based keys, while the Reducer aggregates these batches to compute the final dot product for the target matrix.

---

<!-- FEATURES -->
<a name="features"></a>
## Features

| Feature | Description |
|---------|-------------|
| **Parallel Computing** | Implements distributed matrix multiplication logic via MapReduce. |
| **Coordinate Mapping** | Mapper dynamically expands elements based on target result cell coordinates. |
| **Efficient Aggregation** | Reducer performs memory-efficient dot product calculations. |
| **Local Simulation** | Supports local execution using standard UNIX pipe-based simulations. |
| **Archival Quality** | Integrated scholarly citation metadata and technical specifications. |

### Tech Stack
- **Language**: Python 3.x
- **Framework**: MapReduce (Distributed Computing)
- **Tooling**: Hadoop Streaming API
- **Batch Processing**: Distributed Matrix Arithmetic

---

<!-- STRUCTURE -->
<a name="project-structure"></a>
## Project Structure

```bash
HADOOP/
│
├── docs/                            # Technical Documentation
│   └── SPECIFICATION.md             # Architecture & Flow Specification
│
├── Source Code/                     # Primary Application Layer
│   ├── HADOOP.ipynb                 # Interactive Experimental Environment
│   ├── mapper.py                    # Map Phase Logic (Partitioning)
│   ├── reducer.py                   # Reduce Phase Logic (Aggregation)
│   ├── input.txt                    # Sample Matrix Input Data
│   └── cache.txt                    # Dimension Configuration Cache
│
├── .gitattributes                   # Git configuration
├── .gitignore                       # Git exclusion manifest
├── CITATION.cff                     # Scholarly Citation Metadata
├── codemeta.json                    # Machine-Readable Project Metadata
├── LICENSE                          # MIT License Terms
├── README.md                        # Comprehensive Archival Entrance
└── SECURITY.md                      # Security Policy & Protocol
```

---

<!-- RESULTS -->
<a name="mapreduce-process-flow"></a>
## MapReduce Process Flow

<div align="center">

  ### Architectural Logic (Map -> Shuffle -> Reduce)
  
  ```mermaid
  graph TD
      Input[("Input Data (Matrix A & B)")] -->|Reads| Mapper["Mapper (mapper.py)"]
      Cache[("Cache (Matrix Dimensions)")] -->|Configures| Mapper
      
      subgraph Map_Phase ["Map Phase"]
          Mapper -->|Partitions| Intermediate["Intermediate Key-Value Pairs"]
          Intermediate -->|Emits| Shuffle["Shuffle & Sort"]
      end
      
      subgraph Reduce_Phase ["Reduce Phase"]
          Shuffle -->|Groups by Key| Reducer["Reducer (reducer.py)"]
          Reducer -->|Dot Product| Result["Result Aggregator"]
      end
      
      Result -->|Writes| Output[("Output (Matrix Product)")]
  ```

</div>

---

<!-- QUICK START -->
<a name="quick-start"></a>
## Quick Start

### 1. Prerequisites
- **Runtime**: Python 3.x installed on your workstation.
- **Environment**: Basic understanding of Hadoop Streaming or local MapReduce simulators.

### 2. Setup & Execution
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Amey-Thakur/HADOOP.git
    cd HADOOP
    ```
2.  **Launch (Local Simulation)**:
    ```bash
    cat "Source Code/input.txt" | python "Source Code/mapper.py" | sort -k1,1 | python "Source Code/reducer.py"
    ```

---

<!-- =========================================================================================
                                     USAGE SECTION
     ========================================================================================= -->
## Usage Guidelines

This repository is openly shared to support learning and knowledge exchange across the academic community.

**For Students**  
Use this project as a reference for understanding distributed data representations, intermediate key mapping, and the practical implementation of the MapReduce paradigm.

**For Educators**  
This project serves as a foundational case study for Big Data Analytics (Course Code: `CSDLO7032` and `CSL704`). Attribution is appreciated when utilizing content.

**For Researchers**  
The technical specification and metadata provide insights into the implementation of distributed arithmetic architectures and the partitioning of datasets for high-scale computational tasks.

---

<!-- LICENSE -->
<a name="license"></a>
## License

This repository and all its creative and technical assets are made available under the **MIT License**. See the [LICENSE](LICENSE) file for complete terms.

> [!NOTE]
> **Summary**: You are free to share and adapt this content for any purpose, even commercially, as long as you provide appropriate attribution to the original author.

Copyright © 2021 Amey Thakur

---

<!-- ABOUT -->
<a name="about-this-repository"></a>
## About This Repository

**Created & Maintained by**: [Amey Thakur](https://github.com/Amey-Thakur)  
**Academic Journey**: Bachelor of Engineering in Computer Engineering (2018-2022)  
**Institution**: [Terna Engineering College](https://ternaengg.ac.in/), Navi Mumbai  
**University**: [University of Mumbai](https://mu.ac.in/)

This project features the **HADOOP Matrix Multiplication**, an application developed during my explorations in Big Data Analytics. It highlights the use of distributed computing paradigms to build scalable, parallelized computational solutions.

**Connect**: [GitHub](https://github.com/Amey-Thakur) · [LinkedIn](https://www.linkedin.com/in/amey-thakur) · [ORCID](https://orcid.org/0000-0001-5644-1575)

### Acknowledgments

Special thanks to the mentors and peers who supported this learning endeavor during the Big Data Analytics laboratory sessions at Terna Engineering College.

---

<div align="center">

  [↑ Back to Top](#readme-top)

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#mapreduce-process-flow) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

  <br>

  🔬 **[Big Data Analytics & Computational Lab - I](https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I)** &nbsp;·&nbsp; 🐘 **[HADOOP](https://github.com/Amey-Thakur/HADOOP)**

  ---

  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
