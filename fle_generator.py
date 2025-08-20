# FLE Course Generator - Optimized English Prompts for French Output
# Leverages your full English proficiency while ensuring French content quality

class FLECourseGenerator:
    def __init__(self):
        self.base_variables = {
            "level": ["A1", "A2", "B1", "B2"],
            "age": ["12-14 years", "15-17 years", "18+ years"],
            "source_language": ["German", "English", "Italian"],
            "duration": ["45 min", "90 min", "3-lesson sequence"],
            "skill_focus": ["grammar", "vocabulary", "speaking", "listening", "writing"]
        }
        
        # French output instruction template
        self.french_output_base = """
**CRITICAL OUTPUT REQUIREMENTS:**
- Provide ALL content in French
- Use proper FLE (Français Langue Étrangère) terminology
- Include specific notes for German-speaking learners where relevant
- Highlight typical German-speaker difficulties (false friends, grammar interference, pronunciation)
- Use authentic, natural French throughout
- Format everything ready for classroom use
"""

    def comprehensive_lesson_template(self, **kwargs):
        """Template for complete lesson planning"""
        return f"""
# COMPREHENSIVE FLE LESSON GENERATOR

**PEDAGOGICAL CONTEXT:**
- Level: {kwargs.get('level', 'B1')}
- Learner age: {kwargs.get('age', '15-17 years')}
- Source language: {kwargs.get('source_language', 'German')}
- Lesson duration: {kwargs.get('duration', '45 minutes')}
- Class size: {kwargs.get('class_size', '15-20 students')}
- Teaching context: {kwargs.get('context', 'Secondary school in German-speaking Switzerland')}

**PRIMARY OBJECTIVE:**
{kwargs.get('objective', 'Develop spontaneous oral expression')}

**SPECIFIC CHALLENGES FOR GERMAN SPEAKERS:**
{kwargs.get('german_difficulties', 'pronunciation patterns, grammatical gender, past tense formation, false friends')}

**PEDAGOGICAL APPROACH:**
- Communicative methodology prioritized
- Avoid traditional "school-like" drilling
- Encourage authentic communication
- Build confidence through success-oriented activities

**LESSON STRUCTURE REQUIRED:**
1. **Warm-up** (5-10 min): Activation activity
2. **Discovery** (15-20 min): New content presentation
3. **Guided practice** (15 min): Semi-controlled exercises
4. **Free production** (10 min): Spontaneous expression
5. **Wrap-up** (5 min): Summary and homework

**DETAILED OUTPUT FORMAT:**
For each phase, provide:
- Activity title (catchy and engaging)
- Required materials (simple, accessible)
- Step-by-step teacher instructions
- Clear student instructions
- Differentiation options (easier/harder variants)
- Anticipated errors and correction strategies
- Timing guidelines
- Assessment opportunities

**SPECIAL ADAPTATIONS:**
- Include phonetic guidance for difficult French sounds
- Provide German-French comparison charts where helpful
- Suggest visual aids and memory techniques
- Consider cultural references accessible to German-speaking teens

**ENGAGEMENT FACTORS:**
Create activities that naturally encourage students to speak without fear of making mistakes. Focus on meaning over form initially, then integrate accuracy work naturally.

{self.french_output_base}
"""

    def targeted_activity_template(self, **kwargs):
        """Template for specific skill-focused activities"""
        return f"""
# TARGETED FLE ACTIVITY GENERATOR

**ACTIVITY PARAMETERS:**
- Target skill: {kwargs.get('skill', 'Oral expression')}
- Grammar focus: {kwargs.get('grammar', 'Passé composé')}
- Vocabulary theme: {kwargs.get('theme', 'Describing past experiences')}
- Student level: {kwargs.get('level', 'B1')}
- Activity duration: {kwargs.get('duration', '20 minutes')}
- Interaction pattern: {kwargs.get('interaction', 'Pair work and class discussion')}

**TECHNICAL CONSTRAINTS:**
- Create engaging activity that promotes SPONTANEOUS communication
- Natural integration of: {kwargs.get('grammar', 'target grammar point')}
- Address typical German-speaker errors in this area
- Use minimal technology (accessible materials only)
- Include clear success criteria

**ACTIVITY FRAMEWORK:**
1. **Setup** (How to introduce and motivate the activity)
2. **Clear instructions** (Step-by-step breakdown)
3. **Execution** (What students actually do)
4. **Teacher role** (Monitoring, helping, correcting strategies)
5. **Follow-up** (How to exploit student productions)
6. **Extension** (Optional deeper exploration)

**DIFFERENTIATION STRATEGIES:**
- Simplified version for struggling students
- Challenge extensions for advanced learners
- Visual supports and scaffolding options
- Alternative ways to participate (for shy students)

**GERMAN-SPEAKER SPECIFIC ADAPTATIONS:**
- Anticipate L1 interference patterns
- Provide contrastive examples where helpful
- Include pronunciation practice if relevant
- Address false friends or grammar confusion

**FORMATIVE ASSESSMENT:**
How to observe and correct without disrupting natural communication flow? Include both accuracy and fluency considerations.

**MATERIALS AND SETUP:**
Specify exactly what you need and how to arrange the classroom for maximum effectiveness.

{self.french_output_base}
"""

    def material_creation_template(self, **kwargs):
        """Template for creating pedagogical materials"""
        return f"""
# FLE TEACHING MATERIAL GENERATOR

**MATERIAL TYPE:** {kwargs.get('material_type', 'Vocabulary worksheet')}
**TARGET CONTEXT:** {kwargs.get('context', 'B1 class, 16-year-olds, German speakers')}

**SPECIFICATIONS:**
- Format: {kwargs.get('format', 'A4, black and white printable')}
- Visual elements: {kwargs.get('visuals', 'Simple diagrams, no complex images')}
- Interactivity: {kwargs.get('interactivity', 'Fill-in spaces, matching exercises')}
- Difficulty progression: {kwargs.get('progression', 'Easy to challenging within same material')}

**CONTENT REQUIREMENTS:**
{kwargs.get('specific_content', 'Vocabulary introduction + practice exercises + mini communication task')}

**GERMAN-SPEAKER ADAPTATIONS:**
- Highlight false friends with German
- Include phonetic transcription for difficult words
- Provide comparative structures when helpful
- Add cultural context notes where appropriate

**TEACHER SUPPORT MATERIALS:**
- Answer keys (separate page)
- Teaching suggestions and timing
- Extension activities
- Troubleshooting common difficulties

**STUDENT-FRIENDLY FEATURES:**
- Clear, attractive layout
- Logical progression
- Self-check opportunities
- Motivating content relevant to teenage interests

**PRACTICAL CONSIDERATIONS:**
- Easy to photocopy and distribute
- Minimal preparation time required
- Reusable for different classes
- Adaptable for homework or classwork

{self.french_output_base}

**ADDITIONAL INSTRUCTION:**
Create complete, ready-to-use material that I can immediately print and use in class tomorrow.
"""

    def assessment_rubric_template(self, **kwargs):
        """Template for creating assessment tools"""
        return f"""
# FLE ASSESSMENT RUBRIC GENERATOR

**ASSESSMENT CONTEXT:**
- Skill being evaluated: {kwargs.get('skill', 'Oral presentation')}
- Student level: {kwargs.get('level', 'B1')}
- Assessment type: {kwargs.get('assessment_type', 'Formative peer assessment')}
- Age group: {kwargs.get('age', '15-17 years')}

**RUBRIC REQUIREMENTS:**
- {kwargs.get('criteria_count', '4-5')} clear criteria
- {kwargs.get('scale', '4-point scale')} (1=Beginning, 2=Developing, 3=Proficient, 4=Advanced)
- Student-friendly language
- Specific, observable descriptors
- Encouraging tone that promotes growth

**SPECIFIC FOCUS AREAS:**
1. {kwargs.get('criterion1', 'Fluency and spontaneity')}
2. {kwargs.get('criterion2', 'Accuracy (grammar and vocabulary)')}
3. {kwargs.get('criterion3', 'Pronunciation and intonation')}
4. {kwargs.get('criterion4', 'Communication effectiveness')}

**GERMAN-SPEAKER CONSIDERATIONS:**
- Acknowledge common L1 interference without penalizing
- Recognize effort in overcoming typical difficulties
- Balance accuracy expectations with communication success
- Include progress indicators specific to German→French challenges

**RUBRIC FEATURES:**
- Self-assessment version for students
- Peer assessment adaptation
- Teacher version with additional notes
- Goal-setting section for improvement

**PRACTICAL APPLICATION:**
- Quick to use during class
- Helpful for student feedback
- Supports learning rather than just ranking
- Clear connection to lesson objectives

{self.french_output_base}

**TONE REQUIREMENT:**
Create an encouraging, growth-oriented assessment tool that motivates students while providing clear feedback on their French learning progress.
"""

    def generate_custom_prompt(self, template_type, **kwargs):
        """Generate customized prompt based on type"""
        if template_type == "lesson":
            return self.comprehensive_lesson_template(**kwargs)
        elif template_type == "activity":
            return self.targeted_activity_template(**kwargs)
        elif template_type == "material":
            return self.material_creation_template(**kwargs)
        elif template_type == "assessment":
            return self.assessment_rubric_template(**kwargs)
        else:
            return "Template type not recognized. Available: lesson, activity, material, assessment"

# PRACTICAL USAGE EXAMPLES
generator = FLECourseGenerator()

# Example 1: Complete lesson for intermediate students
lesson_prompt = generator.generate_custom_prompt(
    "lesson",
    level="B1",
    age="16-18 years",
    objective="Express opinions about environmental issues using subjunctive",
    duration="90 minutes",
    german_difficulties="subjunctive vs indicative confusion, opinion expression patterns"
)

print("=== LESSON TEMPLATE ===")
print(lesson_prompt)
print("\n" + "="*60 + "\n")

# Example 2: Targeted speaking activity
activity_prompt = generator.generate_custom_prompt(
    "activity",
    skill="Interactive speaking",
    grammar="Future tense (futur simple vs futur proche)",
    theme="Making plans and predictions",
    level="A2",
    duration="25 minutes"
)

print("=== ACTIVITY TEMPLATE ===")
print(activity_prompt)
print("\n" + "="*60 + "\n")

# Example 3: Assessment rubric
assessment_prompt = generator.generate_custom_prompt(
    "assessment",
    skill="Written expression",
    level="B1",
    assessment_type="Summative essay evaluation",
    criterion1="Task completion and content",
    criterion2="Text organization and coherence",
    criterion3="Grammar accuracy and range",
    criterion4="Vocabulary appropriateness and variety"
)

print("=== ASSESSMENT TEMPLATE ===")
print(assessment_prompt)

# Batch generation function for efficiency
def generate_lesson_series(theme, levels=["A1", "A2", "B1"]):
    """Generate a series of lessons on the same theme for different levels"""
    prompts = []
    for level in levels:
        prompt = generator.generate_custom_prompt(
            "lesson",
            level=level,
            objective=f"Communicate about {theme} at {level} level",
            theme=theme
        )
        prompts.append((level, prompt))
    return prompts

# Example: Generate family-themed lessons for all levels
print("\n=== BATCH GENERATION EXAMPLE ===")
family_series = generate_lesson_series("family relationships")
for level, prompt in family_series:
    print(f"\n--- {level} LEVEL PROMPT ---")
    print(prompt[:300] + "...\n")
