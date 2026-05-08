---
name: deck-llm
description: Machine learning for deck analysis using PyTorch neural networks
---
# Deck LLM (Language Model)

- **Purpose**
  
  Machine learning utilities for Yu-Gi-Oh! deck analysis and modeling using PyTorch. Provides neural network components, card embeddings, and training examples for deck-based language models.

- **Core Components**

  - **[nn.py](nn.py)** — Neural network utilities and building blocks
    - Custom PyTorch modules and tensor operations
    - Attention mechanisms (Flash Attention support)
    - Embedding functions with Qwen3-Embedding integration
    - PCA dimensionality reduction
    - Various activation functions (SwiGLU, SoftmaxGLU)
    
  - **[ygonn.py](ygonn.py)** — YGO-specific neural network features
    - Card database integration (SQLite cards.cdb)
    - Card embedding generation
    - Deck loading and preprocessing
    - Feature extraction for cards
    - Bindings and aliases management
    
  - **[bindx5c.py](bindx5c.py)** — Bind card ID prediction model
    - Lightning-based training example
    - Predicts 5-card bind combinations
    - Uses attention mechanism for sequence prediction
    
  - **[open.py](open.py)** — Open vocabulary model
    - Alternative model architecture
    - Card feature embedding model
    - Training example for deck generation

- **Requirements**

  - PyTorch with CUDA support
  - Flash Attention (optional, for performance)
  - Lightning AI framework
  - SQLite database (cards.cdb)
  - YGOPro installation with card data
  
- **Usage Examples**

  ```python
  from ygonn import cardsfeat, decks
  
  # Load card features
  features = cardsfeat()
  
  # Load deck data
  deck_tensors = decks()
  
  # Train model (example)
  model = Model()
  trainer = L.Trainer(precision=16)
  trainer.fit(model, DataLoader(decks(), ...))
  ```

- **Integration Skills**

  Used by:
  - `ygo/card-build/SKILL.md` — For ML-assisted card design
  - `ygo/deck/analyze/SKILL.md` — For deck pattern recognition
  - `ygo/meta/predict/SKILL.md` — For meta trend prediction
  
- **Customization**

  - Modify embedding models in `ygonn.py`
  - Adjust model architectures in examples
  - Add custom training objectives
  - Integrate with other YGO data sources

- **Performance Notes**

  - Models benefit from GPU acceleration
  - Use mixed precision (FP16) for training
  - Flash Attention significantly speeds up attention layers
  - PCA reduces feature dimensionality for efficiency