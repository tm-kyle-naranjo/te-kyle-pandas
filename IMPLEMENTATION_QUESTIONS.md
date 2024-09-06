# Implementation Questions

## 1. Why perform validation checks before data cleaning?

Validation checks are performed before data cleaning for several reasons:

Validation checks are performed before data cleaning for several important reasons. Early error detection allows for quicker problem resolution and prevents the propagation of errors throughout the pipeline. By halting the process for critical errors, computational resources are saved that would otherwise be wasted on cleaning invalid data. This approach ensures that the input data meets basic quality standards before any transformations are applied, maintaining data integrity. Additionally, performing validation checks first allows the cleaning process to be tailored based on the validation results, making the overall data processing more efficient and effective.

## 2. Classification of issues as ERRORS vs WARNINGS

ERRORS are severe issues that halt the pipeline, including missing required columns, invalid data types in critical columns, and completely invalid timestamp formats. These problems fundamentally compromise the data structure and meaning, making further processing unreliable or impossible.

On the other hand, WARNINGS are less critical issues that allow the pipeline to proceed. These include the presence of null values, minor timestamp format inconsistencies (if convertible), duplicate entries, and whitespace issues. Such problems can often be addressed in the cleaning stage without compromising the overall data integrity, allowing for a more flexible and efficient data processing workflow.

## 3. Redesigning data architecture for DailyCheckins

This redesigned architecture addresses critical shortcomings in the previous data platforms lab, which lacked any validation or cleaning steps. The absence of these crucial processes in the earlier design could lead to severe data integrity issues if the raw CSV files contained errors, potentially compromising the entire data pipeline and resulting in unreliable analytics.

The new process begins with data ingestion, loading raw data into a staging area. Next, a validation asset performs rigorous checks, outputs a detailed report, and handles errors and warnings appropriately. This step is vital in catching and addressing data quality issues early, preventing the propagation of errors downstream. A cleaning asset then applies necessary operations based on validation results, producing cleaned and standardized data. Finally, a load asset transfers the cleaned data into the DailyCheckins table, completing the workflow.

+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Raw CSV Files |---->|  Data Ingestion|---->|   Validation   |---->|    Cleaning    |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
                                                      |                      |
                                                      |                      |
                                              +----------------+     +----------------+
                                              |                |     |                |
                                              | Error Handling |     |  Load to Daily |
                                              |   & Reporting  |     |   Checkins DB  |
                                              |                |     |                |
                                              +----------------+     +----------------+

This robust architecture ensures a systematic approach to data processing, maintaining data integrity and efficiency throughout the pipeline. By implementing these validation and cleaning steps, we significantly reduce the risk of corrupted or inaccurate data entering the system, thereby enhancing the reliability and usefulness of subsequent analyses and reports generated from the DailyCheckins table.