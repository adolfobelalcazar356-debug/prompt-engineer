# Compact Examples

These examples show shape, not mandatory templates. Preserve the user's language unless they request another language.

## SIMPLE — direct

Input:
> Cambia el texto del botón Guardar por Confirmar. Nada más.

Optimized:
> Cambia únicamente el texto visible del botón `Guardar` a `Confirmar`. Preserva su comportamiento, estilos y cualquier lógica asociada; no realices otros cambios.

## BOUNDED DEBUG — explore first

Input:
> El login falla después de varias horas. Arréglalo.

Optimized:
> Investiga el fallo del login que aparece después de sesiones prolongadas. Antes de editar, revisa la implementación, manejo de sesión/token y tests relacionados; reproduce o identifica la causa raíz con evidencia. Corrige únicamente la causa encontrada, preserva el flujo de autenticación no relacionado y añade/ajusta cobertura de regresión. Termina cuando la corrección esté verificada y los tests relevantes pasen.

## COMPLEX — plan first

Input:
> Crea un módulo de aprobaciones con roles, niveles, notificaciones y auditoría.

Optimized:
> Antes de implementar, inspecciona la arquitectura y los flujos actuales y prepara un plan acotado para el nuevo módulo de aprobaciones. Identifica integraciones, datos afectados, restricciones existentes y decisiones faltantes. No inventes jerarquías, reglas de autorización ni políticas de negocio no definidas. Expón las decisiones críticas que requieren confirmación y define criterios verificables de éxito antes de proponer cambios de código.

## AUDIT

Input:
> Mejora el rendimiento del módulo.

Audit shape:
- **Route:** `ASK_USER` o `EXPLORE_FIRST`, según el contexto disponible.
- **Blocking gap:** no se define qué operación está lenta ni cómo demostrar mejora.
- **Risk:** optimizar sin evidencia puede cambiar código irrelevante.
- **Next:** inspeccionar métricas/perfilado disponibles; si el objetivo sigue ambiguo, hacer una sola pregunta crítica.

## GENERAL — research

Input:
> Investiga proveedores para esta solución y dime cuál escoger.

Optimized:
> Investiga opciones que satisfagan los requisitos y restricciones proporcionados. Separa hechos verificables de inferencias, compara las alternativas con criterios consistentes, señala información faltante que pueda cambiar la decisión y termina con una recomendación justificada. No inventes requisitos que no estén en el contexto.
