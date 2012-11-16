from warnings import warn

class EvaluationResult(object):
    """An object that stores the results output by trec_eval. 
    """

    eval_fields = {"num_q": int,
                   "num_ret": int,
                   "num_rel": int,
                   "num_rel_ret": int,
                   "map": float,
                   "gm_map": float,
                   "Rprec": float,
                   "bpref": float,
                   "recip_rank": float,
                   "iprec_at_recall_0.00": float,
                   "iprec_at_recall_0.10": float,
                   "iprec_at_recall_0.20": float,
                   "iprec_at_recall_0.30": float,
                   "iprec_at_recall_0.40": float,
                   "iprec_at_recall_0.50": float,
                   "iprec_at_recall_0.60": float,
                   "iprec_at_recall_0.70": float,
                   "iprec_at_recall_0.80": float,
                   "iprec_at_recall_0.90": float,
                   "iprec_at_recall_1.00": float,
                   "P_5": float,
                   "P_10": float,
                   "P_15": float,
                   "P_20": float,
                   "P_30": float,
                   "P_100": float,
                   "P_200": float,
                   "P_500": float,
                   "P_1000": float}

    def __init__(self, filepath):
        """Initializes from a file which contains the output from trec_eval.
        """
        self.runid = ""
        self.results = {}
        self.queries = {}

        with open(filepath, 'r') as f:
            for line in f:
                if line.isspace():
                    continue
                (field, query, value) = line.split()
                if query == "all": #accumulated results over all queries
                    if field == "runid":
                        self.runid = value
                    else:
                        self.parse_field(field, value, self.results)
                else:
                    if not query in self.queries:
                        self.queries[query] = {}
                    self.parse_field(field, value, self.queries[query])

    def parse_field(self, field, value, target):
        """Parses the value of a field and puts it in target[field]."""
        field_types = self.__class__.eval_fields

        if field in field_types:
            target[field] = field_types[field](value)
        else:
            warn("Skipping unknown field `%s`."%field) 


                    






