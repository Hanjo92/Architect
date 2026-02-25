# Web-App Naming and Comment Conventions

Use this reference when the target project is a web-app service.

## Naming Rules

- Use intention-revealing names; avoid vague names like `data`, `manager`, `util`, `temp`.
- Use domain vocabulary in modules, services, events, and errors.
- Use verb-first names for functions (`createSession`, `validateToken`, `publishEvent`).
- Use readable booleans (`isActive`, `hasAccess`, `canRetry`).
- Keep folder/package names feature-first and consistent with bounded contexts.

## Function Comment Rules

- Add concise comments for non-trivial public functions.
- Explain intent and business meaning, not implementation trivia.
- Keep to 1-2 lines summary, then add parameters/returns/exceptions when relevant.

## Language-Specific Style

- C#: XML documentation (`summary`, `param`, `returns`, `exception`).
- TypeScript: TSDoc (`@param`, `@returns`, `@throws`).
- JavaScript: JSDoc (`@param`, `@returns`, `@throws`).

## Example (TypeScript)

```ts
/**
 * Validate payment command against current account state and return domain-safe result.
 * @param state Current account state.
 * @param command Payment command from API.
 * @returns Validation result with accepted/rejected reason.
 */
export function validatePayment(state: AccountState, command: PaymentCommand): ValidationResult {
  // ...
}
```
