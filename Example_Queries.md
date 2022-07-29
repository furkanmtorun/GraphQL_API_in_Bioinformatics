# 🧪 Basic GraphQL API for an Example Bioinformatics Case

## Data Schema

**Are you looking for an daily life analogy instead of `gene`, `transcript`, `expression_profiles` terms?**

You could think of an <b>author</b> instead of a <b>gene</b>. So, our authors (genes) might have more than one <b>book (transcript)</b>. Also, each <b>book (transcript)</b> could have more than one version/type and - so, their meta information also change!

<br>

## Example Queries
Here, I provided some queries to demonstrate the use of GraphQL API. 
Feel free to play around with them to learn more!

Example Gene IDs: `GeneID1`, `GeneID2`
Example Gene Names: `GeneName1`, `GeneName2`
Example Transcript IDs: `TranscriptID1.1`, `TranscriptID1.2`, `TranscriptID1.3`, `TranscriptID2.1`, `TranscriptID2.2`

<br>

### Query all the genes and transcript IDs of each gene
```
query {
  genes {
    gene_id
    gene_name
    gene_description
    transcripts {
      transcript_id
    }
  }
}
```

### Query the all transcripts, their lengths and expression profiles for "GeneName1":
```
query {
  genes(gene_name: "GeneName1") {
    gene_id
    gene_name
    gene_description
    transcripts {
      transcript_id
      length
      expression_profiles {
        brain
        heart
      }
    }
  }
}
```

### Query all the transcripts for the gene with the `gene_id` of "GeneID2"
```
query {
  transcripts(gene_id: "GeneID2") {
    gene_id
    transcript_id
    length
  }
}
```

### Query the expression profile for the transcript with the `transcript_id` of "TranscriptID2.1"
```
query {
  expression_profiles(transcript_id: "TranscriptID2.1"){
    transcript_id
    brain
    heart
  }
}
```
