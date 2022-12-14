"""BASIC TEST UTILITY FOR CHECKING IF A QUERY IS WORKING AND PROVIDING THE EXPECTED RESULT"""
import requests
import pytest

# SET VARIABLES
GRAPHQL_API_ENDPOINT = "http://localhost:5000/graphql"

# DEFINE QUERIES
query_for_all_genes = """ query { genes { gene_id gene_name } } """
query_for_all_transcripts = """ query { transcripts(gene_id: "GeneID1") { transcript_id length } } """
query_for_single_transcript = """ query { transcripts(transcript_id: "TranscriptID1.1") { transcript_id length } } """
query_for_expression_profile_for_single_transcript = """ query { expression_profiles(transcript_id: "TranscriptID2.1"){ transcript_id brain heart } } """

# DEFINE EXPECTED RESULTS
expected_result_for_all_genes = {'data': {'genes': [{'gene_id': 'GeneID1', 'gene_name': 'GeneName1'}, {'gene_id': 'GeneID2', 'gene_name': 'GeneName2'}]}}
expected_result_for_all_transcripts = { "data": { "transcripts": [ { "length": 101, "transcript_id": "TranscriptID1.1" }, { "length": 102, "transcript_id": "TranscriptID1.2" }, { "length": 103, "transcript_id": "TranscriptID1.3" } ] } }
expected_result_for_single_transcript = { "data": { "transcripts": [ { "length": 101, "transcript_id": "TranscriptID1.1" } ] } }
expected_result_for_expression_profile_for_single_transcript = { "data": { "expression_profiles": [ { "brain": 201.201, "heart": 2.01, "transcript_id": "TranscriptID2.1" } ] } }

def check_query_and_expected_result(query, expected_result):
    response = requests.post(GRAPHQL_API_ENDPOINT, json={'query': query}, timeout=None)
    assert response.status_code == 200, "Query failed"
    assert response.json() == expected_result, "Results did NOT match"
    
# TEST QUERIES AND EXPECTED RESULTS
all_queries = [query_for_all_genes, query_for_all_transcripts, query_for_single_transcript, 
               query_for_expression_profile_for_single_transcript]
all_expected_results = [expected_result_for_all_genes, expected_result_for_all_transcripts, 
                        expected_result_for_single_transcript, expected_result_for_expression_profile_for_single_transcript]

# RUN TESTS
def test_all_queries():
    for query, expected_result in zip(all_queries, all_expected_results):
        check_query_and_expected_result(query, expected_result)
