# Permissions and Groups

## Custom Permissions
- `can_view`: Allows viewing of books.
- `can_create`: Allows creation of books.
- `can_edit`: Allows editing of books.
- `can_delete`: Allows deletion of books.

## Groups
- **Viewers**: Can view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Full access to all actions.

## Enforcing Permissions
- Function-based views: Use `@permission_required`.
- Class-based views: Use `PermissionRequiredMixin`.

## Testing
- Create test users and assign them to groups.
- Verify users can only access views or actions based on their group permissions.

## Automating Group Setup
Run the following command to set up groups and permissions:
```bash
python manage.py setup_groups
