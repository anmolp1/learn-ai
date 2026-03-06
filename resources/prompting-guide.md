# Prompting Patterns Reference

A quick reference for the prompting patterns taught in Session 1. Bookmark this and use it as a cheat sheet.

## Pattern 1: Structured Prompt

Give AI clear context, constraints, and output format.

```
You are a [role with relevant expertise].

I need you to [specific task].

Context:
- [Relevant background information]
- [Current situation]
- [Any constraints or requirements]

Output format:
- [What you want back: code, list, document, etc.]
- [Any formatting requirements]
```

**When to use:** Almost always. This is your default pattern.

## Pattern 2: Chain-of-Thought

Ask AI to reason through a problem step by step.

```
I need to [task/decision].

Before giving me your recommendation, please:
1. List the key factors to consider
2. Analyze each factor
3. Walk through your reasoning
4. Then give your recommendation with justification
```

**When to use:** Complex decisions, debugging, analysis tasks.

## Pattern 3: Few-Shot Examples

Show AI what good output looks like before asking it to produce.

```
I need you to [task]. Here are examples of the output I want:

Example 1:
Input: [example input]
Output: [example output]

Example 2:
Input: [example input]
Output: [example output]

Now do the same for:
Input: [your actual input]
```

**When to use:** When you have a specific format or style in mind.

## Pattern 4: Iterative Refinement

Don't accept the first response. Give specific feedback and iterate.

```
[After receiving initial output]

Good start. Please make these specific changes:
1. [Change 1]
2. [Change 2]
3. [Change 3]

Keep everything else the same.
```

**When to use:** Always. The first response is a draft, not a final product.

## Pattern 5: Role Assignment

Give AI a specific persona for domain-relevant output.

```
Act as a senior [role] with 10 years of experience in [domain].

Review the following [artifact] and provide:
- Issues you see (ranked by severity)
- Specific recommendations to fix each issue
- Any best practices that are missing

[Paste artifact here]
```

**When to use:** Code review, content editing, strategy feedback — any task where domain expertise matters.

## Anti-Patterns (What Not to Do)

1. **The vague prompt:** "Help me with my project" → Too broad. Be specific about what help you need.
2. **The essay prompt:** 500 words of context with no clear ask → Put the task upfront, context below.
3. **The one-and-done:** Accepting the first response without review → Always iterate at least once.
4. **The copy-paste-ship:** Using AI output without reading it → Read everything. Test everything.
5. **The over-delegation:** "Build me an entire app" → Break tasks into steps. AI works best on focused tasks.
