# fle-ai-generator
Smart prompt templates for FLE teachers to generate professional French lessons and activities using AI. English-powered prompts optimized for German-speaking learners, delivering native-quality French educational content in minutes.

## Features

- **4 specialized templates**: Complete lessons, targeted activities, teaching materials, and assessment rubrics
- **German-speaker optimized**: Built-in adaptations for common L1 interference patterns
- **Professional output**: AI generates native-level French content with proper FLE terminology
- **Time-saving**: Turn 2-hour lesson prep into 10-minute AI-assisted creation
- **Flexible parameters**: Easily customize level (A1-B2), age groups, objectives, and duration

## Quick Start

```python
from fle_generator import FLECourseGenerator

generator = FLECourseGenerator()

# Generate a complete B1 lesson
prompt = generator.generate_custom_prompt(
    "lesson",
    level="B1", 
    objective="Express opinions about environmental issues",
    duration="90 minutes"
)

# Copy prompt to ChatGPT/Claude → Get full French lesson plan!
