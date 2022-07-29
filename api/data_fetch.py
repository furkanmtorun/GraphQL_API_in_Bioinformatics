"""Data Fetching from the DB

Here, it could be possible to fetch data from any sort of DB (MySQL, Sqlite) here.
However, to make this basic API simpler and to not being out of scope, I defined them here.
"""

all_genes = [
    {"gene_id": "GeneID1", "gene_name": "GeneName1", "gene_description": "GeneDesc1"},
    {"gene_id": "GeneID2", "gene_name": "GeneName2", "gene_description": "GeneDesc2"},
]

all_transcripts = [
    {"gene_id": "GeneID1", "transcript_id": "TranscriptID1.1", "length": 101},
    {"gene_id": "GeneID1", "transcript_id": "TranscriptID1.2", "length": 102},
    {"gene_id": "GeneID1", "transcript_id": "TranscriptID1.3", "length": 103},
    {"gene_id": "GeneID2", "transcript_id": "TranscriptID2.1", "length": 201},
    {"gene_id": "GeneID2", "transcript_id": "TranscriptID2.2", "length": 202},
]

all_expression_profiles = [
    {"transcript_id": "TranscriptID1.1", "brain": 101.101, "heart": 1.01},
    {"transcript_id": "TranscriptID1.2", "brain": 102.102, "heart": 1.02},
    {"transcript_id": "TranscriptID1.3", "brain": 103.103, "heart": 1.03},
    {"transcript_id": "TranscriptID2.1", "brain": 201.201, "heart": 2.01},
    {"transcript_id": "TranscriptID2.2", "brain": 202.202, "heart": 2.02},
]
