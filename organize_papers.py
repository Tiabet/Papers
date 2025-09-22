#!/usr/bin/env python3
import re
import shutil
from pathlib import Path

ROOT = Path(r"c:/Development/Paper")
DEFAULT_FOLDER = "99_Misc"

RULES = {
    "RAG": [
        ("00_Surveys_Overviews", r"(survey|bestpractice|beyond|research|discussion|overview|taxonomy|landscape|discus|guide|review)"),
        ("01_Graph_RAG", r"(graph|grag|graph-?rag|g-?retriever|kg2rag|regraph|t-grag|node|pg-rag|knowledge\s*graph|kgqa|hetero)"),
        ("02_MultiHop_Path", r"(multihop|multi-hop|hoprag|pathrag|reasoning\spaths?|chain\sof\sthought|planner|route|decompos)"),
        ("03_Efficient_RAG", r"(fast|lean|light|efficien|raptor|sufficient|mini|universal|cache|stream|scalable|accelerat|latency|compress|budget|retriev)"),
        ("04_Specialized_Methods", r"(hippo|hyde|ircot|dpr|logic|hybrid|blendedrag|archrag|meteora|mindmap|query2doc|rag(?=$|[+.\-_0-9])|sirerag|rqrag|rwg|cov-?rag|llm|instruct|badrag|mdqa|rat|surge)"),
    ],
    "\ub525\ub7ec\ub2dd\uc804\ubc18": [
        ("00_Optimization", r"(optimizer|adam|pgd|cpo|cw)"),
        ("01_Normalization", r"(normaliz)"),
        ("02_ModelArchitectures", r"(resnet|lstm|rnn|transformer|diffusion|fourier)"),
        ("03_Data_Quality", r"(evaluation|selection|tidy|outlier|missing)"),
        ("04_Foundation_Models", r"(deepseek|tulu|xsns|rethink|coz|model)"),
    ],
    "\uc5f0\uad6c": [
        ("00_Surveys_Textbooks", r"(survey|textbook|review|reasoninglm|overview|tutorial)"),
        ("01_KG_Construction", r"(kgc|kgt|extract|ontology|orkg|construct|kgdm|knowledge\s*graph|entity|relation|spert|kopa|gnp|holmes)"),
        ("02_RAG_for_KG", r"(rag|qa|pkg|hiprag|th-rag|llm|mdqa|gkg)"),
        ("03_Diffusion_Generative", r"(diff|fdm|score|denoise)"),
        ("04_Temporal_Multimodal", r"(temporal|tkg|multimodal|amr|dynamic|spatio)"),
    ],
    "\uc790\uc5f0\uc5b4\ucc98\ub9ac": [
        ("00_Attention_Architecture", r"(attention|transformer|seq2seq|lstm|bert|gpt|xl|bahadanau|moe|mixture|encoder|decoder)"),
        ("01_Foundation_Models", r"(model|llm|scaling|bloom|vllm|icl|incontext|context\s*learning|foundation)"),
        ("02_Training_Optimization", r"(training|efficient|lora|qlora|peft|distill|compute|bm25|retriev|rerank|optimization|searchr1)"),
        ("03_Prompting_Agentic", r"(prompt|cot|pal|spiqa|chain|agent|tooluse|planner|workflow)"),
        ("04_Evaluation_Detection", r"(classification|hallucinate|market|benchmark|dataset|zeroshot|zero-shot|generalization|evaluate|cepe|eli5|gqa|accuracy|judge)"),
        ("05_RLHF_Alignment", r"(preference|rl|deepseek|alignment|reward)"),
        ("06_Embeddings", r"(embed|wordpiece|sentence|embedding|vector)"),
    ],
    "\uc885\uc1241\ub17c\ubb38\uad00\ub828": [
        ("00_TimeSeries", r"(informer|tft|pyraformer|timeseries|tprnn)"),
        ("01_Unlearning", r"(unlearning)"),
        ("02_Representation", r"(dimension|transformer|representation)"),
        ("03_Normalization", r"(normaliz|normali)"),
        ("04_KoreanResources", r"[\uac00-\ud7a3]"),
    ],
    "\uc885\uc1242\ub17c\ubb38\uad00\ub828": [
        ("00_Adversarial_Attacks", r"(fgsm|pgd|attack)"),
        ("01_Deepfake_Detection", r"(deepfake|dsfd|mtcnn|flm|anda|apaa)"),
        ("02_Defense_Strategies", r"(nightshade|poison|breaker|obstruct)"),
        ("03_Metrics_Quality", r"(ssim|quality)"),
    ],
}

def organize(root: Path, rules):
    if not root.exists():
        print(f"Skipping {root}, not found")
        return
    print(f"Organizing {root}")
    for entry in sorted(root.iterdir()):
        if entry.is_file() and entry.suffix.lower() == ".pdf":
            lname = entry.name.lower()
            target = DEFAULT_FOLDER
            for sub, pattern in rules:
                if re.search(pattern, lname):
                    target = sub
                    break
            dest_dir = root / target
            dest_dir.mkdir(exist_ok=True)
            dest = dest_dir / entry.name
            print(f"  Moving {entry.name} -> {target}")
            shutil.move(str(entry), str(dest))

if __name__ == "__main__":
    for folder, rule in RULES.items():
        organize(ROOT / folder, rule)
