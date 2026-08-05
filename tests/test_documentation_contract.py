import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class ProductDesignReviewDocumentationTest(unittest.TestCase):
    def test_product_design_review_reference_exists_with_actionable_report_contract(self) -> None:
        path = ROOT / "references" / "product-design-review.md"
        self.assertTrue(path.exists())
        content = path.read_text(encoding="utf-8")

        for required in (
            "Existing Product Design Review",
            "Review Mode Routing",
            "Evidence Protocol",
            "Product UI Deep Audit",
            "Anti-AI Design Tell Check",
            "Review Workflow",
            "Before/After Comparison",
            "Competitive Or Reference Comparison",
            "Scorecard",
            "Mode-Specific Findings",
            "Actionable Improvements",
            "Improvement Tracks",
            "Acceptance Criteria",
            "Verification Checklist",
            "Chinese Report Template",
        ):
            self.assertIn(required, content)

        self.assertIn("do not implement changes unless", content)
        self.assertIn("Ground every major finding in observable evidence", content)
        self.assertIn("P0", content)
        self.assertIn("P1", content)
        self.assertIn("P2", content)
        self.assertIn("what to change, why it matters, how to change it", content)

    def test_anti_ai_design_tells_reference_exists_for_product_and_marketing_reviews(self) -> None:
        path = ROOT / "references" / "anti-ai-design-tells.md"
        self.assertTrue(path.exists())
        content = path.read_text(encoding="utf-8")

        for required in (
            "Anti-AI Design Tell Review",
            "High-Confidence Tells",
            "Product UI Tells",
            "Marketing And Conversion Tells",
            "Recommendation Rule",
            "Do Not Overapply",
        ):
            self.assertIn(required, content)

        self.assertIn("Default AI purple/blue gradients", content)
        self.assertIn("Marketing-page hero structure used for an operational tool", content)
        self.assertIn("do not copy taste-skill landing-page bans blindly", content.lower())

    def test_skill_routes_existing_design_reviews_to_both_review_references(self) -> None:
        skill = read("SKILL.md")

        self.assertIn("references/product-design-review.md", skill)
        self.assertIn("references/review-rubric.md", skill)
        self.assertIn("references/anti-ai-design-tells.md", skill)
        self.assertRegex(
            skill,
            re.compile(
                r"evaluate existing design.*product-design-review\.md.*review-rubric\.md",
                re.IGNORECASE | re.DOTALL,
            ),
        )
        self.assertIn("classify the review mode", skill)
        self.assertIn("prioritized, evidence-backed recommendations", skill)
        self.assertIn("verification steps", skill)

    def test_readmes_advertise_existing_product_design_evaluation(self) -> None:
        english = read("README.md")
        chinese = read("README.zh-CN.md")

        self.assertIn("Evaluates existing product/page designs by mode", english)
        self.assertIn("flags generic AI-design tells", english)
        self.assertIn("Evaluate an existing product/page design", english)
        self.assertIn("marketing pages, product workbenches, data dashboards", english)
        self.assertIn("product-design-review.md", english)
        self.assertIn("anti-ai-design-tells.md", english)

        self.assertIn("评估已有产品", chinese)
        self.assertIn("模板化 AI 设计痕迹", chinese)
        self.assertIn("评估已有产品或页面设计", chinese)
        self.assertIn("营销页、产品工作台、数据仪表盘", chinese)
        self.assertIn("product-design-review.md", chinese)
        self.assertIn("anti-ai-design-tells.md", chinese)

    def test_helper_registry_lists_optional_evidence_helpers_for_design_review(self) -> None:
        registry = read("references/helper-registry.md")

        self.assertIn("Product design reviews use `f-design`", registry)
        self.assertIn("Existing product/page design evaluation", registry)
        self.assertIn("web-design-guidelines", registry)
        self.assertIn("webapp-testing", registry)
        self.assertIn("design-taste-frontend` only", registry)

    def test_review_rubric_links_mode_extensions_and_anti_ai_checks(self) -> None:
        rubric = read("references/review-rubric.md")

        self.assertIn("references/product-design-review.md", rubric)
        self.assertIn("references/anti-ai-design-tells.md", rubric)
        self.assertIn("Mode Extensions", rubric)
        self.assertIn("Product workbench", rubric)
        self.assertIn("Marketing page", rubric)


if __name__ == "__main__":
    unittest.main()
