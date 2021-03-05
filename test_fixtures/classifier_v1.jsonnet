{
  dataset_reader: {
    lazy: false,
    type: 'text_classification_json',
    tokenizer: {
      type: 'konoha',
      tokenizer_name: 'janome',
    },
    token_indexers: {
      tokens: {
        type: 'single_id',
        lowercase_tokens: true,
      },
    },
  },
  datasets_for_vocab_creation: ['train'],
  train_data_path: 'https://konoha-demo.s3-ap-northeast-1.amazonaws.com/himkt-tweet/train.jsonl',
  validation_data_path: 'https://konoha-demo.s3-ap-northeast-1.amazonaws.com/himkt-tweet/test.jsonl',
  model: {
    type: 'basic_classifier',
    text_field_embedder: {
      token_embedders: {
        tokens: {
          embedding_dim: 32,
        },
      },
    },
    seq2vec_encoder: {
      type: 'cnn',
      num_filters: 32,
      embedding_dim: 32,
      output_dim: 32,
    },
    dropout: 0.3,
  },
  data_loader: {
    batch_size: 10,
  },

  trainer: {
    cuda_device: -1,
    num_epochs: 5,
    optimizer: {
      lr: 0.1,
      type: 'adam',
    },
    validation_metric: '+accuracy',
  },
}

