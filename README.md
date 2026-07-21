# lld_python_practice

Personal practice repo for Python OOP, low-level design (LLD), and system design interview prep.

## Structure

### `python_exercises/`
A guided, step-by-step curriculum: Python classes and OOP mechanics → SOLID principles → API
development (FastAPI) and pagination → design patterns. Each lesson is a standalone,
runnable `.py` file with TODOs to fill in. See [python_exercises/readme.md](python_exercises/readme.md)
for the full lesson list and progress.

```
python python_exercises/lesson_01_classes.py
```

### LLD practice projects
Small object-oriented systems designed and implemented end-to-end, following the
requirements → entities → class design → implementation flow described in `framework.txt`.

<<<<<<< HEAD
| Project | Description |
|---|---|
| [`amazon_locker/`](amazon_locker/) | Amazon-style parcel locker system — locker/compartment allocation, sizing, access tokens. |
| [`connect_four/`](connect_four/) | Connect Four game engine — board, turn-based play, win detection. See its own [readme](connect_four/readme.txt) for requirements and class design. |
| [`elevator/`](elevator/) | Elevator control system — request handling and dispatch logic. |

### Design & concurrency notes
Reference notes used while studying for LLD and concurrency interviews:

| File | Topic |
|---|---|
| [`oop.txt`](oop.txt) | Encapsulation, abstraction, polymorphism, inheritance — core OOP principles with interview framing. |
| [`design_patterns.txt`](design_patterns.txt) | Creational, structural, and behavioral design patterns. |
| [`framework.txt`](framework.txt) | The requirements → entities → class design → implementation → extensibility delivery framework used across the LLD projects above. |
| [`concurrency.txt`](concurrency.txt) / [`concurrency_in_python.md`](concurrency_in_python.md) | Concurrency fundamentals, in general and Python-specific. |
| [`coordination.txt`](coordination.txt) | Coordinating work between threads/services (producer-consumer, signaling). |
| [`correctness.txt`](correctness.txt) | Preventing data corruption under concurrent access. |
| [`scarcity.txt`](scarcity.txt) | Managing limited/shared resources (connection pools, caches, etc.). |

### `resume_builder/`
Standalone personal utility (unrelated to the LLD/OOP practice above) for generating resume
variants from structured data.

## Setup

A virtualenv is checked out at `.venv/`. Activate it before running anything:

```powershell
.venv\Scripts\Activate.ps1
```
=======
### Design & concurrency notes
Reference notes used while studying for LLD and concurrency interviews
>>>>>>> e4837894246606eb05ddb39a1042c6371c3ad75c
