import pkg_resources

np_version = pkg_resources.get_distribution("numpy").version

print(f"numpy version: {np_version}")