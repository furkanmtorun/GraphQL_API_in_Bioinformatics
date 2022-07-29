"""Contains DB queries and resolver functions"""

# Query all items from the DB, see the file for explanations
from .data_fetch import all_genes, all_transcripts, all_expression_profiles

# Resolvers for the fields
def resolve_genes(obj, info, gene_id=None, gene_name=None):
    try:
        if gene_id:
            payload = [item for item in all_genes if item["gene_id"] == gene_id]
        elif gene_name:
            payload = [item for item in all_genes if item["gene_name"] == gene_name]
        else:
            payload = all_genes
    except Exception as error:
        payload = [str(error)]
    return payload


def resolve_transcripts(obj, info, gene_id=None, transcript_id=None):
    try:
        if gene_id:
            payload = [item for item in all_transcripts if item["gene_id"] == gene_id]
        elif transcript_id:
            payload = [
                item
                for item in all_transcripts
                if item["transcript_id"] == transcript_id
            ]
        else:
            payload = [
                item
                for item in all_transcripts
                if item["gene_id"] == str(obj["gene_id"])
            ]
    except Exception as error:
        payload = [str(error)]
    return payload


def resolve_expression_profiles(obj, info, transcript_id=None):
    try:
        if transcript_id:
            payload = [
                item
                for item in all_expression_profiles
                if item["transcript_id"] == transcript_id
            ]
        else:
            payload = [
                item
                for item in all_expression_profiles
                if item["transcript_id"] == str(obj["transcript_id"])
            ]
    except Exception as error:
        payload = [str(error)]
    return payload
