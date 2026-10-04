# FreeLLMAPI - Complete Provider List

**Source:** https://github.com/tashfeenahmed/freellmapi

This document contains a comprehensive list of all 34+ free LLM providers integrated into FreeLLMAPI with 635+ free model endpoints and ~7.4 billion tokens per month.

---

## 📋 All Supported Providers (34+)

### 1. **Google Gemini**
- **Platform ID:** `google`
- **Base URL:** `https://generativelanguage.googleapis.com/v1beta`
- **Type:** Native Gemini API format
- **Features:** Unique wire format, extended timeout (60s for reasoning models)
- **Auth:** API key
- **Free Tier:** Yes

### 2. **Groq**
- **Platform ID:** `groq`
- **Base URL:** `https://api.groq.com/openai/v1`
- **Type:** OpenAI-compatible
- **Features:** High-speed inference
- **Auth:** API key
- **Free Tier:** Yes

### 3. **Cerebras**
- **Platform ID:** `cerebras`
- **Base URL:** `https://api.cerebras.ai/v1`
- **Type:** OpenAI-compatible
- **Auth:** API key
- **Free Tier:** Yes

### 4. **Sail Research**
- **Platform ID:** `sail`
- **Base URL:** `https://api.sailresearch.com/v1`
- **Type:** Responses API (custom adapter)
- **Features:** Background job submission, polling-based
- **Free Credits:** $5/month (payment method required)
- **Auth:** Bearer token

### 5. **Aclide**
- **Platform ID:** `aclide`
- **Type:** OpenAI-compatible gateway
- **Auth:** API key

### 6. **Speka**
- **Platform ID:** `speka`
- **Base URL:** `https://speka.me/v1`
- **Type:** OpenAI-compatible
- **Free Tier:** $1/month (shared across chat & embeddings)
- **Auth:** API key

### 7. **LLMTR**
- **Platform ID:** `llmtr`
- **Base URL:** `https://llmtr.com/v1`
- **Type:** OpenAI-compatible
- **Features:** Daily/rolling quota models
- **Auth:** API key

### 8. **Gizmo**
- **Platform ID:** `gizmo`
- **Type:** OpenAI-compatible
- **Auth:** API key

### 9. **BlockRun**
- **Platform ID:** `blockrun`
- **Type:** OpenAI-compatible
- **Auth:** API key

### 10. **Moondream**
- **Platform ID:** `moondream`
- **Type:** Vision-specialized
- **Auth:** API key

### 11. **ElectronHub**
- **Platform ID:** `electronhub`
- **Type:** OpenAI-compatible
- **Features:** Shared wallet free plans
- **Auth:** API key

### 12. **Experiential**
- **Platform ID:** `experiential`
- **Type:** OpenAI-compatible
- **Auth:** API key

### 13. **Router9**
- **Platform ID:** `router9`
- **Type:** OpenAI-compatible aggregator
- **Features:** Shared monthly credits
- **Auth:** API key

### 14. **Septor**
- **Platform ID:** `septor`
- **Type:** OpenAI-compatible
- **Features:** Daily quota, one-time signup credit
- **Auth:** API key

### 15. **CLōD**
- **Platform ID:** `clod`
- **Base URL:** `https://api.clod.io/v1`
- **Type:** OpenAI-compatible
- **Auth:** API key

### 16. **Speechify**
- **Platform ID:** `speechify`
- **Type:** Speech/TTS-specialized
- **Auth:** API key

### 17. **Blaze**
- **Platform ID:** `blaze`
- **Type:** OpenAI-compatible
- **Auth:** API key

### 18. **Lucidity**
- **Platform ID:** `lucidity`
- **Type:** OpenAI-compatible gateway
- **Features:** Pins response model to requested route
- **Auth:** API key

### 19. **Airforce**
- **Platform ID:** `airforce`
- **Type:** OpenAI-compatible gateway
- **Auth:** API key

### 20. **DreamPrompting**
- **Platform ID:** `dreamprompting`
- **Type:** OpenAI-compatible gateway
- **Auth:** API key

### 21. **Waterfall**
- **Platform ID:** `waterfall`
- **Type:** OpenAI-compatible gateway
- **Auth:** API key

### 22. **Logfare**
- **Platform ID:** `logfare`
- **Type:** OpenAI-compatible gateway
- **Auth:** API key

### 23. **B.AI**
- **Platform ID:** `bai`
- **Base URL:** `https://api.b.ai/v1`
- **Type:** OpenAI-compatible
- **Features:** Limited-time promo models
- **Auth:** API key

### 24. **AnyAPI**
- **Platform ID:** `anyapi`
- **Base URL:** `https://api.anyapi.ai/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Tier:** $0, no card, 100K tokens/day
- **Auth:** API key

### 25. **AMD Radeon Cloud**
- **Platform ID:** `radeon`
- **Base URL:** `https://developer.amd.com.cn/radeon/api/v1`
- **Type:** OpenAI-compatible
- **Features:** Single tool calls only, 10-minute timeout
- **Free Tier:** GPU-time-based quota
- **Auth:** API key

### 26. **NVIDIA NIM**
- **Platform ID:** `nvidia`
- **Base URL:** `https://integrate.api.nvidia.com/v1`
- **Type:** OpenAI-compatible
- **Features:** Single tool calls, 180s timeout for reasoning models
- **Free Tier:** Yes
- **Auth:** API key

### 27. **Mistral**
- **Platform ID:** `mistral`
- **Base URL:** `https://api.mistral.ai/v1`
- **Type:** OpenAI-compatible
- **Auth:** API key
- **Free Tier:** Yes

### 28. **OpenRouter**
- **Platform ID:** `openrouter`
- **Base URL:** `https://openrouter.ai/api/v1`
- **Type:** OpenAI-compatible aggregator
- **Features:** Extra headers (HTTP-Referer, X-Title)
- **Auth:** API key
- **Free Tier:** Yes

### 29. **GitHub Models**
- **Platform ID:** `github`
- **Base URL:** `https://models.github.ai/inference`
- **Type:** OpenAI-compatible
- **Auth:** GitHub token
- **Free Tier:** Yes

### 30. **Cohere**
- **Platform ID:** `cohere`
- **Type:** OpenAI-compatible via compatibility endpoint (custom adapter)
- **Auth:** API key
- **Free Tier:** Yes

### 31. **Cloudflare Workers AI**
- **Platform ID:** `cloudflare`
- **Type:** OpenAI-compatible (custom adapter)
- **Auth:** account_id:token
- **Free Tier:** Yes

### 32. **Zhipu (Z.ai / BigModel.cn)**
- **Platform ID:** `zhipu`
- **Base URL:** `https://open.bigmodel.cn/api/paas/v4` (domestic) or `https://api.z.ai/v1` (global)
- **Type:** OpenAI-compatible (custom adapter with auto-detection)
- **Features:** Hidden reasoning support, 60s timeout
- **Auth:** API key
- **Free Tier:** Yes

### 33. **HuggingFace Router**
- **Platform ID:** `huggingface`
- **Base URL:** `https://router.huggingface.co/v1`
- **Type:** OpenAI-compatible
- **Free Tier:** $0.10/month recurring credit
- **Auth:** API key

### 34. **Ollama Cloud**
- **Platform ID:** `ollama`
- **Base URL:** `https://ollama.com/v1`
- **Type:** OpenAI-compatible
- **Features:** 1 concurrent model, 5h session caps, 120s timeout
- **Free Tier:** GPU-time-based quota
- **Auth:** API key

---

## Additional Providers (17+)

### 35. **Kilo AI Gateway**
- **Platform ID:** `kilo`
- **Base URL:** `https://api.kilo.ai/api/gateway/v1`
- **Type:** OpenAI-compatible aggregator (keyless)
- **Free Tier:** 200 req/hr per IP (anonymous)
- **Auth:** Optional (keyless support)

### 36. **Pollinations**
- **Platform ID:** `pollinations`
- **Base URL:** `https://gen.pollinations.ai/v1`
- **Type:** OpenAI-compatible (custom adapter)
- **Features:** Shared-capacity tier, 1 pollen/IP/hour
- **Auth:** API key
- **Free Tier:** Yes

### 37. **LLM7.io**
- **Platform ID:** `llm7`
- **Base URL:** `https://api.llm7.io/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Tier:** 100 req/hr (anonymous access also works)
- **Auth:** API key (optional)

### 38. **OpenCode Zen**
- **Platform ID:** `opencode`
- **Base URL:** `https://opencode.ai/zen/v1`
- **Type:** OpenAI-compatible gateway
- **Features:** Limited-time promotional models
- **Auth:** API key
- **Note:** Free tier limited to OpenCode client as of 2026-09

### 39. **OVH AI Endpoints**
- **Platform ID:** `ovh`
- **Base URL:** `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`
- **Type:** OpenAI-compatible (keyless)
- **Free Tier:** 2 req/min per IP (anonymous), 400 req/min (authenticated)
- **Auth:** Optional (keyless support)

### 40. **Agnes AI (Sapiens AI)**
- **Platform ID:** `agnes`
- **Base URL:** `https://apihub.agnes-ai.com/v1`
- **Type:** OpenAI-compatible
- **Features:** Proprietary models, 60s timeout for reasoning
- **Free Tier:** $0/token (promotional)
- **Auth:** API key

### 41. **Reka**
- **Platform ID:** `reka`
- **Base URL:** `https://api.reka.ai/v1`
- **Type:** OpenAI-compatible
- **Features:** Text reasoning & multimodal support
- **Auth:** API key
- **Note:** Requires prepaid credits (legacy free tiers retired)

### 42. **SiliconFlow**
- **Platform ID:** `siliconflow`
- **Base URL:** `https://api.siliconflow.com/v1`
- **Type:** OpenAI-compatible
- **Features:** Free generative media models (FLUX.1, CosyVoice2)
- **Auth:** API key
- **Free Tier:** Yes

### 43. **Routeway**
- **Platform ID:** `routeway`
- **Base URL:** `https://api.routeway.ai/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Tier:** $0 `:free` models, 5-20 rpm limit
- **Auth:** API key
- **Features:** Browser User-Agent required

### 44. **BazaarLink**
- **Platform ID:** `bazaarlink`
- **Base URL:** `https://bazaarlink.ai/api/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Model:** `auto:free` route only
- **Auth:** API key
- **Free Tier:** Yes

### 45. **AINative Studio**
- **Platform ID:** `ainative`
- **Base URL:** `https://api.ainative.studio/api/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Tier:** ~10M tokens/month (unverified)
- **Auth:** Bearer or X-API-Key
- **Note:** Accept both Bearer auth and X-API-Key header

### 46. **Aion Labs**
- **Platform ID:** `aion`
- **Base URL:** `https://api.aionlabs.ai/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Tier:** Yes (catalog-managed)
- **Auth:** API key

### 47. **Requesty**
- **Platform ID:** `requesty`
- **Base URL:** `https://router.requesty.ai/v1`
- **Type:** OpenAI-compatible router
- **Free Tier:** Yes
- **Auth:** API key

### 48. **NavyAI**
- **Platform ID:** `navy`
- **Base URL:** `https://api.navy/v1`
- **Type:** OpenAI-compatible unified API
- **Free Tier:** 150K tokens/day, 20 RPM
- **Auth:** API key (Discord-backed)
- **Features:** Requires explicit User-Agent header

### 49. **NaraRouter**
- **Platform ID:** `nara`
- **Base URL:** `https://router.bynara.id/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Tier:** Yes (requires Telegram verification)
- **Auth:** API key
- **Note:** Requires Telegram channel/link verification

### 50. **SEA-LION (AI Singapore)**
- **Platform ID:** `sealion`
- **Base URL:** `https://api.sea-lion.ai/v1`
- **Type:** OpenAI-compatible first-party API
- **Free Tier:** 10 RPM
- **Auth:** API key (Google sign-in)
- **Note:** No regional restrictions, available globally

### 51. **OrcaRouter**
- **Platform ID:** `orcarouter`
- **Base URL:** `https://api.orcarouter.ai/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Models:** `*-free` suffix models, $0 cost
- **Free Tier:** Yes (unpublished rate limits, 429 on cap)
- **Auth:** API key (`sk-orca-` prefix)
- **Features:** Free routes never fall back to paid

### 52. **UnoRouter**
- **Platform ID:** `unorouter`
- **Base URL:** `https://api.unorouter.com/v1`
- **Type:** OpenAI-compatible aggregator
- **Free Models:** `*:free` suffix only
- **Free Tier:** 1 request/minute per account per model
- **Auth:** API key
- **Note:** Parallel requests trigger account-wide cooldown

### 53. **xKiro**
- **Platform ID:** `xkiro`
- **Base URL:** `https://api.xkiro.com/v1`
- **Type:** OpenAI-compatible gateway
- **Free Tier:** 5,000,000 tokens/day
- **Auth:** Bearer or x-api-key header
- **Validation URL:** `https://api.xkiro.com/v1/usage`

---

## Chinese Domestic Providers (4)

> **Note:** These require Chinese real-name verification except LongCat

### 54. **Baidu Qianfan (百度千帆)**
- **Platform ID:** `qianfan`
- **Base URL:** `https://qianfan.baidubce.com/v2`
- **Type:** OpenAI-compatible
- **Models:** ERNIE-Speed / ERNIE-Lite / ERNIE-Tiny
- **Free Tier:** Pay-as-you-go billing
- **Auth:** API key

### 55. **Volcengine Ark (火山方舟, ByteDance)**
- **Platform ID:** `volcengine`
- **Base URL:** `https://ark.cn-beijing.volces.com/api/v3`
- **Type:** OpenAI-compatible
- **Free Tier:** 2M tokens/day per model (recurring)
- **Auth:** API key
- **Target:** Individual developers

### 56. **LongCat (Meituan / 美团)**
- **Platform ID:** `longcat`
- **Base URL:** `https://api.longcat.chat/openai/v1`
- **Type:** OpenAI-compatible
- **Free Tier:** Daily free quota
- **Auth:** Email signup (no region restriction)
- **Note:** Only provider NOT requiring Chinese verification

### 57. **iFlytek Spark (讯飞星火)**
- **Platform ID:** `xfyun`
- **Base URL:** `https://spark-api-open.xf-yun.com/v1`
- **Type:** OpenAI-compatible
- **Free Model:** Lite model only
- **Auth:** Console APIPassword as Bearer token

---

## Special Providers

### 58. **ModelScope (魔搭社区, Alibaba)**
- **Platform ID:** `modelscope`
- **Base URL:** `https://api-inference.modelscope.cn/v1`
- **Type:** OpenAI-compatible (custom adapter)
- **Free Tier:** 2000 requests/day account-wide
- **Requirement:** Bind to Alibaba Cloud China account with real-name verification
- **Auth:** Bearer token
- **Note:** Unbound tokens get 401 error

### 59. **AI Horde**
- **Platform ID:** `aihorde`
- **Base URL:** Community-powered inference
- **Type:** OpenAI-compatible (custom adapter)
- **Features:** Queue-based, keyless/anonymous
- **Free Tier:** Anonymous (0000000000 key), registered keys get higher priority
- **Limitations:** max_tokens ≥16, stop must be array, no tool calling, 120s timeout
- **Usage Units:** Kudos (synthesized to tokens)

### 60. **Custom OpenAI-Compatible Endpoints**
- **Platform ID:** `custom`
- **Type:** User-supplied base URL
- **Supported Tools:** Chat, embeddings, images, audio
- **Examples:** 
  - llama.cpp
  - LM Studio
  - vLLM
  - Ollama (local)
  - Any remote gateway
- **Timeout:** 120 seconds (for slow local inference)
- **Auth:** User-supplied key

---

## 📊 Provider Statistics

| Metric | Value |
|--------|-------|
| **Total Providers** | 37+ dedicated + 1 custom |
| **OpenAI-Compatible** | ~27 providers |
| **Custom Adapters** | ~10 providers |
| **Keyless Providers** | 3 (Kilo, OVH, AI Horde) |
| **Total Free Model Endpoints** | 635+ |
| **Chat Models** | 584 |
| **Embedding Models** | 41 |
| **Transcription Models** | 7 |
| **Video Models** | 3 |
| **Monthly Free Tokens** | ~7.4 billion |

---

## 🔑 Authentication Methods

- **API Keys:** Most providers (40+)
- **Bearer Tokens:** Cohere, Mistral, Huggingface, etc.
- **Custom Headers:** Some require User-Agent, referers
- **Keyless:** Kilo, OVH, AI Horde (anonymous access)
- **GitHub Tokens:** GitHub Models
- **Discord-backed:** NavyAI

---

## ⚙️ Provider Features

### Timeout Configurations
- **Google Gemini:** 60 seconds (reasoning models)
- **NVIDIA NIM:** 180 seconds (reasoning models)
- **Agnes AI:** 60 seconds (reasoning models)
- **Ollama Cloud:** 120 seconds (reasoning models)
- **Custom Endpoints:** 120 seconds (local inference)
- **Default:** 15 seconds

### Special Adapters
- **Google:** Native Gemini API format
- **Sail Research:** Background job submission + polling
- **Cohere:** Dedicated compatibility adapter
- **Cloudflare:** Custom account_id:token format
- **Zhipu:** Auto-detection between domestic & global endpoints
- **Pollinations:** Account/key validation via `/account/key`
- **ModelScope:** Chat probe for validation
- **AI Horde:** Queue-based, kudos-to-tokens conversion

---

## 🚀 Quick Integration

```typescript
// Example: Adding FreeLLMAPI to your project
import { FreeLLMAPI } from 'freellmapi';

const client = new FreeLLMAPI({
  baseUrl: 'http://localhost:3001/v1',
  apiKey: 'freellmapi-your-unified-key'
});

// Automatically routes to best available free model
const response = await client.chat.completions.create({
  model: 'auto', // Let router pick
  messages: [{ role: 'user', content: 'Hello!' }]
});
```

---

## 📚 Additional Resources

- **Official Website:** https://freellmapi.co
- **Models Directory:** https://freellmapi.co/models.html
- **GitHub Repository:** https://github.com/tashfeenahmed/freellmapi
- **Documentation:** https://github.com/tashfeenahmed/freellmapi/tree/main/docs/en
- **Provider Details:** https://github.com/tashfeenahmed/freellmapi/blob/main/server/src/providers/index.ts

---

## ⚠️ Important Notes

1. **Personal Experimentation Only:** This project is for prototyping, not production
2. **No SLA:** Variable latency, free tiers have limitations
3. **ToS Compliance:** Each provider's ToS reviewed (see GitHub docs)
4. **Model Catalog:** Self-updating (premium users get live feed)
5. **Auto-Failover:** Intelligent routing with cooldowns and key rotation
6. **Encryption:** Provider keys stored as AES-256-GCM encrypted at rest

---

**Last Updated:** October 4, 2026  
**Source:** https://github.com/tashfeenahmed/freellmapi
