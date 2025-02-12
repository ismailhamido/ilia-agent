import pkg_resources

try:
    pkg_resources.get_distribution('Auto-GPT')
    print('Auto-GPT is installed')
except pkg_resources.DistributionNotFound:
    print('Auto-GPT is NOT installed')

try:
    pkg_resources.get_distribution('LangChain')
    print('LangChain is installed')
except pkg_resources.DistributionNotFound:
    print('LangChain is NOT installed')