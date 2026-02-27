# AGENTS.md instructions for this workspace

<INSTRUCTIONS>
## Skills
A skill is a set of local instructions to follow that is stored in a `SKILL.md` file.

### Available skills
- project-structure-design: Design project structure and system architecture for game/web-app projects. Includes DDD/ECS split for games, Unity UPM modularization, planning augmentation, domain extraction, migration playbook/task board, and validation gates. (file: skills/project-structure-design/SKILL.md)

### How to use skills
- Trigger rules: If the user names a skill (with `$SkillName` or plain text) OR the task clearly matches a skill description above, use that skill for that turn.
- Use skill content progressively: read `SKILL.md` first, then load only required `references/` files.
- Prefer bundled scripts/templates from the skill over re-writing large boilerplate.
</INSTRUCTIONS>
