"""
Main entry into the library
"""


def init_param_sampleprovider():
    import pyarex.parameter_sample_provider as psp
    return psp.ParameterSampleProvider()


def init_param_jobresultretriever():
    import pyarex.parameter_job_result_retriever as pjrr
    return pjrr.ParameterJobResultRetriever()


def init_aresjob(**kwargs):
    import pyarex.ares_job as aj
    return aj.AresJob(**kwargs)

