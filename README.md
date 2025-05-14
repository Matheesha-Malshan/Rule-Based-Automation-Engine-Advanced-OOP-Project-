## UML Class Diagram

<img src="project/umlclass.png" alt="UML Class Diagram"/>


A modular, rule-based automation engine inspired by IFTTT — designed using advanced Python OOP concepts including metaclasses, custom triggers, and action pipelines.
It watches a directory for .csv file creations and deletions, and responds with user-defined actions such as logging or deleting files.

Features
✅ Metaclass-based Trigger Registration
Dynamically register new triggers using a custom metaclass without modifying central registries.

✅ Event-Driven Engine
Modular Trigger, Rule, and Action classes encapsulate functionality for clean and scalable architecture.

✅ Logging System
Centralized logger with support for different levels (info, warning, error) written to a log file.

✅ Multi-threaded Execution
Threaded rule execution for responsive, concurrent event handling.

✅ Context Manager Support
Engine uses with statement for graceful startup and shutdown.

✅ PEP8 Compliant
Code follows Python's PEP8 style guide for readability and consistency.

