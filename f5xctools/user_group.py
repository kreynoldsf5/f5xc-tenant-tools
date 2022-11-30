from f5xctools.helpers import CreateError, ReplaceError, DelError

def create(xcsession, name: str, nsRoles: str = None, description: str = None):
    try:
        payload = {
            'name': name,
            'description': description,
            'namespace_roles': nsRoles
        }
        resp = xcsession.post(
            '/api/web/custom/namespaces/system/user_groups',
            json=payload
        )
        resp.raise_for_status()
        return
    except Exception as e:
        raise CreateError(e)

def updateUsers(xcsession, name: str, usernames: list):
    try:
        payload = {
            'name': name,
            'username': usernames
        }
        resp = xcsession.put(
            '/api/web/custom/namespaces/system/user_groups',
            json=payload
        )
        resp.raise_for_status()
        return
    except Exception as e:
        raise ReplaceError(e)

def updateRoles(xcsession, name: str, NSroles: list):
    try:
        payload = {
            'name': name,
            'namespace_roles': NSroles
        }
        resp = xcsession.put(
            '/api/web/custom/namespaces/system/user_groups',
            json=payload
        )
        resp.raise_for_status()
        return
    except Exception as e:
        raise ReplaceError(e)

def delete(xcsession, name: str):
    try:
        resp = xcsession.delete(
            '/api/web/custom/namespaces/system/user_groups/{}'.format(name)
        )
        resp.raise_for_status()
        return
    except Exception as e:
        raise DelError(e)
