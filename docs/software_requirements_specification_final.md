# Overview
This document outlines the comprehensive software requirements for the Calculator App project, including both functional and non-functional requirements necessary for its development and successful deployment.

# Software Requirements
This section details the specific functional and non-functional requirements that define the Calculator App's features and performance characteristics.

## Functional Requirements

### Basic Arithmetic Operations
|  ID   | Requirement  |
| :---: | :----------- |
| FR1   | The calculator shall perform addition operations. |
| FR2   | The calculator shall perform subtraction operations. |
| FR3   | The calculator shall perform multiplication operations. |
| FR4   | The calculator shall perform division operations and display an error when dividing by zero. |
| FR5   | The calculator shall display results in real-time as the user inputs data. |

### Scientific Calculations
|  ID   | Requirement  |
| :---: | :----------- |
| FR6   | The calculator shall allow users to perform trigonometric calculations such as `sin`, `cos`, and `tan`. |
| FR7   | The calculator shall support inverse trigonometric calculations when the shift function is activated. |
| FR8   | The calculator shall support hyperbolic functions such as `sinh`, `cosh`, and `tanh`. |
| FR9   | The calculator shall allow users to switch between degree and radian modes. |
| FR10  | The calculator shall provide exponential functions, allowing expressions like `exp(x)`. |

### Memory Functions
|  ID   | Requirement  |
| :---: | :----------- |
| FR11  | The calculator shall allow users to store a value in memory. |
| FR12  | The calculator shall enable users to recall the stored value. |
| FR13  | The calculator shall support adding to the stored memory value (`M+`). |
| FR14  | The calculator shall support subtracting from the stored memory value (`M-`). |
| FR15  | The calculator shall clear the memory upon user command (`MC`). |

### Error Handling
|  ID   | Requirement  |
| :---: | :----------- |
| FR16  | The calculator shall display an error message when invalid input is entered. |
| FR17  | The calculator shall provide a clear button to reset both current and total expressions. |
| FR18  | The calculator shall support a backspace function to delete the last entered character. |
| FR19  | The calculator shall handle input overflow and display appropriate messages when results exceed display capacity. |
| FR20  | The calculator shall not crash when processing undefined expressions. |

### Input Methods
|  ID   | Requirement  |
| :---: | :----------- |
| FR21  | The calculator shall accept keyboard input for all supported functions. |
| FR22  | The calculator shall allow mouse clicks to interact with the buttons on the interface. |
| FR23  | The calculator shall have keyboard shortcuts for basic operations. |
| FR24  | The calculator shall respond to pressing the `Enter` key for evaluating expressions. |
| FR25  | The calculator shall display parentheses as input to support complex expressions. |

## Non-Functional Requirements

### Performance
|  ID    | Requirement  |
| :----: | :----------- |
| NFR1   | The calculator shall respond to user input within 0.5 seconds to ensure smooth performance. |
| NFR2   | The calculator shall handle calculations accurately up to 10 decimal places. |
| NFR3   | The calculator shall perform efficiently without noticeable lag even when performing complex calculations. |
| NFR4   | The calculator shall display results of basic arithmetic operations immediately after input. |
| NFR5   | The calculator shall ensure minimal memory usage during operation. |

### Compatibility
|  ID    | Requirement  |
| :----: | :----------- |
| NFR6   | The calculator shall be compatible with Windows, macOS, and Linux. |
| NFR7   | The calculator shall support different screen resolutions for optimal display. |
| NFR8   | The calculator shall run seamlessly on different versions of the Python runtime environment. |
| NFR9   | The calculator shall maintain functionality across popular desktop environments. |
| NFR10  | The calculator shall be operable without any dependencies on internet connectivity. |

### Usability
|  ID    | Requirement  |
| :----: | :----------- |
| NFR11  | The calculator's user interface shall be intuitive and require minimal learning time. |
| NFR12  | The calculator shall highlight active functions (e.g., degree/radian mode, shift mode). |
| NFR13  | The calculator shall maintain consistent button layout akin to standard calculators. |
| NFR14  | The calculator shall display all outputs clearly in a standard format. |
| NFR15  | The calculator shall provide visual feedback for button presses. |

### Security
|  ID    | Requirement  |
| :----: | :----------- |
| NFR16  | The calculator shall prevent unauthorized access to memory-stored values. |
| NFR17  | The calculator shall sanitize all input to avoid code injection. |
| NFR18  | The calculator shall not store sensitive user data. |
| NFR19  | The calculator shall maintain operational integrity in all states, preventing crashes from abnormal input. |
| NFR20  | The calculator shall provide safe evaluation practices that restrict unintended execution. |

### Maintainability
|  ID    | Requirement  |
| :----: | :----------- |
| NFR21  | The calculator code shall be modular for easy updates and maintenance. |
| NFR22  | The calculator shall be documented with inline comments for major functions. |
| NFR23  | The calculator shall include a comprehensive user manual. |
| NFR24  | The calculator code shall follow PEP 8 guidelines for Python code formatting. |
| NFR25  | The calculator shall support easy bug tracking through error logging. |


# Change Management Plan
This section outlines a comprehensive strategy for integrating the Calculator App into a corporate environment, ensuring seamless adoption and long-term usability. The plan addresses training, integration, and issue resolution, facilitating a smooth transition to using the new application.

## Training Plan
1. **User Training Sessions**: Conduct structured training sessions for engineers and employees. These sessions will cover:
   - Basic operations and navigating the user interface.
   - Advanced features, including scientific and memory functions.
   - Best practices for efficient usage and input management.

2. **Training Materials**:
   - Develop detailed user manuals and video tutorials that guide users through common and advanced functions.
   - Create quick-start guides to provide an overview of key functionalities.
   - Set up an online help center with FAQs and step-by-step instructions.

3. **Hands-on Workshops**:
   - Organize interactive workshops allowing users to practice using the app in real-world scenarios.
   - Provide live demonstrations and one-on-one support for addressing individual queries and challenges.

## Integration into the Existing Ecosystem
1. **Compatibility Assurance**:
   - Test the calculator app thoroughly on all platforms (Windows, macOS, Linux) used by the company to ensure cross-platform compatibility.
   - Conduct pilot programs where select departments use the app and provide feedback on integration challenges.

2. **Software Integration**:
   - Collaborate with IT teams to ensure the app works seamlessly with current tools and software (e.g., productivity suites, data analysis tools).
   - Use APIs or custom scripts, if needed, to enable interaction between the calculator app and other company software.

3. **Security and Compliance**:
   - Ensure the calculator app complies with the company's data security protocols.
   - Implement robust data protection measures, including input validation and prevention of unauthorized access to memory functions.
   - Collaborate with the IT department to verify the app meets all necessary compliance standards.

## Issue Resolution Plan
1. **Dedicated Support Team**:
   - Establish a support team responsible for addressing user issues and concerns. This team will include both internal experts and developers familiar with the app's design and codebase.
   - Implement a ticketing system where users can report bugs or request assistance.

2. **Feedback Loop**:
   - Set up regular feedback channels (e.g., bi-weekly review meetings or a feedback portal) to collect user input and address potential improvements.
   - Encourage users to report both minor and major issues, fostering a culture of continuous improvement.

3. **Bug Tracking and Updates**:
   - Maintain a bug tracking system where reported issues are documented, categorized, and prioritized.
   - Implement a regular update schedule to release patches, improvements, and new features based on user feedback and technological advancements.
   - Ensure all updates are tested in a controlled environment before deployment to prevent disruption in user experience.

4. **Documentation of Known Issues**:
   - Keep an updated list of known issues and workarounds available to users, ensuring transparency and providing immediate solutions while permanent fixes are in progress.

5. **Performance Monitoring**:
   - Use analytics to monitor how the calculator app performs under varying loads and in different scenarios.
   - Regularly review performance metrics to identify any potential inefficiencies or bugs that may affect user experience.

# Traceability Links
This section provides traceability between the software requirements and various software artifacts, ensuring each requirement is linked to relevant diagrams to validate design consistency and completeness.

## Use Case Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| UseCase1 | Basic Operations Use Case | FR1, FR2, FR3, FR4, FR5 |
| UseCase2 | Scientific Calculations Use Case | FR6, FR7, FR8, FR9, FR10 |
| UseCase3 | Memory Functions Use Case | FR11, FR12, FR13, FR14, FR15 |
| UseCase4 | Input and Display Handling | FR21, FR22, FR23, FR24, FR25 |
| UseCase5 | Error Handling Use Case | FR16, FR17, FR18, FR19, FR20 |

## Class Diagram Traceability
| Artifact Name | Requirement ID |
| :-------------: |:----------: |
| Calculator Class | FR1-FR25, NFR1-NFR25 |
| DisplayHandler Class | FR5, FR16, FR17, NFR11-NFR15 |
| MemoryManager Class | FR11-FR15, NFR16-NFR20 |
| InputHandler Class | FR21-FR25, NFR21-NFR25 |
| TrigonometricModule Class | FR6-FR10 |

## Activity Diagram Traceability
| Artifact ID | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| Activity1 | User Input Flow | FR1-FR5, FR21-FR25, NFR2, NFR3 |
| Activity2 | Error Handling Workflow | FR16-FR20, NFR16, NFR19 |
| Activity3 | Memory Function Flow | FR11-FR15, NFR1, NFR5 |
| Activity4 | Calculation Execution | FR6-FR10, NFR4, NFR14 |

# Software Artifacts
This section contains links to the developed software artifacts that support the requirements and design specifications.

* [Class Diagram](https://github.com/chander1925/GVSU-CIS641-Innovators/blob/main/artifacts/Calculator%20APP%20-%20Class%20Diagram.drawio.png)
* [Use Case Diagram](https://github.com/chander1925/GVSU-CIS641-Innovators/blob/main/artifacts/Calculator%20App%20-%20Use%20Case%20Diagram.drawio.png)
* [Activity Diagram](https://github.com/chander1925/GVSU-CIS641-Innovators/blob/main/artifacts/calculatorApp%20-%20Activity%20Diagram.drawio.png)
* [Object Diagram](https://github.com/chander1925/GVSU-CIS641-Innovators/blob/main/artifacts/Object%20Diagram%20(Calculator%20App).jpg)

# Additional Links
* [Assignment 3](https://chander1925.github.io/-CIS641-HW3-digari/)
* [Assignment 2](https://chander1925.github.io/-CIS641-HW2-digari/)
