<div align="center">

  <a name="readme-top"></a>
  # HADOOP | Matrix Multiplication

  [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Completed-success)
  [![Technology](https://img.shields.io/badge/Technology-Python%203%20%7C%20MapReduce-orange)](https://github.com/Amey-Thakur/HADOOP)
  [![Developed by Amey Thakur](https://img.shields.io/badge/Developed%20by-Amey%20Thakur-blue)](https://github.com/Amey-Thakur)

  An implementation of Matrix Multiplication using the MapReduce paradigm in Python, providing a foundation for distributed data processing and large-scale computational arithmetic.

  **[Source Code](Source%20Code/)** &nbsp;·&nbsp; **[Technical Specification](docs/SPECIFICATION.md)** &nbsp;·&nbsp; **[Google Colaboratory](Source%20Code/HADOOP.ipynb)** &nbsp;·&nbsp; **[Live Demo](https://amey-thakur.github.io/HADOOP/)**

</div>

---

<div align="center">

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#system-architecture--process-flow) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

</div>

---

<!-- AUTHORS -->
<div align="center">

  <a name="authors"></a>
  ## Authors

  **Terna Engineering College | Computer Engineering | Batch of 2022**

| <a href="https://github.com/Amey-Thakur"><img src="https://github.com/Amey-Thakur.png" width="150" height="150" alt="Amey Thakur"></a><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-green.svg)](https://orcid.org/0000-0001-5644-1575) |
| :---: |

</div>

---

<!-- OVERVIEW -->
<a name="overview"></a>
## Overview

**HADOOP | Matrix Multiplication** represents a pivotal milestone in the study of the **MapReduce Paradigm**. Developed during the academic study of Big Data Analytics, this project focuses on the practical application of parallel processing to execute large-scale matrix multiplication across distributed environments.

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

```python
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
<a name="system-architecture--process-flow"></a>
## System Architecture & Process Flow

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
- **Environment**: Any modern standards-compliant Unix-like environment for Python execution.

> [!WARNING]
> **Local Execution**
>
> While the project is designed for Hadoop, it can be simulated locally using standard UNIX pipes. Ensure that `input.txt` and `cache.txt` are correctly configured in the `Source Code` directory before execution.

### 2. Setup & Deployment

1.  **Clone the Repository**:
    Start by cloning the project to your local workstation:
    ```bash
    git clone https://github.com/Amey-Thakur/HADOOP.git
    cd HADOOP
    ```

2.  **Initialize Environment**:
    Navigate to the `Source Code` directory where the computational logic resides:
    ```bash
    cd "Source Code"
    ```

3.  **Configure Matrix Dimensions**:
    Verify that `cache.txt` is configured with the correct dimensions (e.g., `2,2` for a 2x2 matrix product):
    ```bash
    # Format: [A_Rows],[B_Cols]
    echo "2,2" > cache.txt
    ```

4.  **Execute Distributed Logic**:
    Simulate the MapReduce pipeline by piping the input through the Mapper and Reducer:
    ```bash
    cat input.txt | python mapper.py | sort -k1,1 | python reducer.py
    ```

---

<!-- =========================================================================================
                                     USAGE SECTION
     ========================================================================================= -->
## Usage Guidelines

This repository is openly shared to support learning and knowledge exchange across the academic community.

**For Students**  
Use this project as reference material for understanding distributed data representations, intermediate key mapping, and the practical implementation of the MapReduce paradigm. The source code is available for study to facilitate self-paced learning and exploration of parallel computing patterns.

**For Educators**  
This project may serve as a practical lab example or supplementary teaching resource for Big Data Analytics (`CSDLO7032` / `CSL704`). Attribution is appreciated when utilizing content.

**For Researchers**  
The documentation and design approach may provide insights into academic project structuring and the implementation of distributed arithmetic architectures.

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

This project features the **HADOOP Matrix Multiplication**, an application developed during my early explorations in Big Data Analytics. It highlights the use of the MapReduce paradigm to build scalable, parallelized computational solutions.

**Connect:** [GitHub](https://github.com/Amey-Thakur) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/amey-thakur) &nbsp;·&nbsp; [ORCID](https://orcid.org/0000-0001-5644-1575)

Grateful acknowledgment to the faculty members of the **Department of Computer Engineering** at Terna Engineering College for their guidance and instruction in Big Data Analytics. Their expertise in distributed systems and parallel processing helped me develop a strong understanding of professional computational development methodologies.

Special thanks to the **mentors and peers** whose encouragement, discussions, and support contributed meaningfully to this learning experience.

---

<div align="center">

  [↑ Back to Top](#readme-top)

  [Authors](#authors) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Features](#features) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Results](#system-architecture--process-flow) &nbsp;·&nbsp; [Quick Start](#quick-start) &nbsp;·&nbsp; [Usage Guidelines](#usage-guidelines) &nbsp;·&nbsp; [License](#license) &nbsp;·&nbsp; [About](#about-this-repository) &nbsp;·&nbsp; [Acknowledgments](#acknowledgments)

  <br>

  🔬 **[Big Data Analytics Laboratory](https://github.com/Amey-Thakur/BIG-DATA-ANALYTICS-AND-COMPUTATIONAL-LAB-I)** &nbsp; · &nbsp; 🐘 **[HADOOP](https://amey-thakur.github.io/HADOOP)**

  ---

  ### 🎓 [Computer Engineering Repository](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING)

  **Computer Engineering (B.E.) - University of Mumbai**

  *Semester-wise curriculum, laboratories, projects, and academic notes.*

</div>
