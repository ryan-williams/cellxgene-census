Python API
==============================

.. currentmodule:: cellxgene_census

.. automodule:: cellxgene_census

Open/retrieve Cell Census data
------------------------------

.. autosummary::
    :toctree: _autosummary/
    :nosignatures:

    cellxgene_census.open_soma
    cellxgene_census.get_default_soma_context
    cellxgene_census.get_source_h5ad_uri
    cellxgene_census.download_source_h5ad


Get slice as AnnData
--------------------
.. autosummary::
    :toctree: _autosummary/
    :nosignatures:

    cellxgene_census.get_anndata

Feature presence matrix
-----------------------
.. autosummary::
    :toctree: _autosummary/
    :nosignatures:

    cellxgene_census.get_presence_matrix

Versioning of Cell Census builds
--------------------------------
.. autosummary::
    :toctree: _autosummary/
    :nosignatures:

    cellxgene_census.get_census_version_description
    cellxgene_census.get_census_version_directory

Experimental: Machine Learning
--------------------------------
.. autosummary::
    :toctree: _autosummary/
    :nosignatures:

    cellxgene_census.experimental.ml.pytorch.experiment_dataloader
    cellxgene_census.experimental.ml.pytorch.ExperimentDataPipe
    cellxgene_census.experimental.ml.pytorch.Stats
    cellxgene_census.experimental.ml.huggingface.CellDatasetBuilder
    cellxgene_census.experimental.ml.huggingface.GeneformerTokenizer

Experimental: Processing
--------------------------------
.. autosummary::
    :toctree: _autosummary/
    :nosignatures:

    cellxgene_census.experimental.pp.get_highly_variable_genes
    cellxgene_census.experimental.pp.highly_variable_genes
    cellxgene_census.experimental.pp.mean_variance

Experimental: Embeddings
--------------------------------
.. autosummary::
    :toctree: _autosummary/
    :nosignatures:

    cellxgene_census.experimental.get_embedding
    cellxgene_census.experimental.get_embedding_metadata
    cellxgene_census.experimental.get_embedding_metadata_by_name
    cellxgene_census.experimental.get_all_available_embeddings
    cellxgene_census.experimental.get_all_census_versions_with_embedding

