"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1


def test_filter_excludes_interaction_with_different_learner_id():
    from datetime import datetime
    from app.models.interaction import InteractionLog

    interactions = [
        InteractionLog(
            id=1, learner_id=2, item_id=1, kind="attempt", timestamp=datetime.now()
        ),
    ]

    result = _filter_by_item_id(interactions, item_id=1)

    assert len(result) == 1


# === AI-GENERATED TESTS ===

def test_filter_by_item_id_large_number():
    """Filter with large item_id value."""
    interactions = [_make_log(1, 1, 999999)]
    result = _filter_by_item_id(interactions, item_id=999999)
    assert len(result) == 1
    assert result[0].id == 1

def test_filter_single_interaction_match():
    """Filter list with single interaction that matches."""
    interactions = [_make_log(5, 10, 3)]
    result = _filter_by_item_id(interactions, item_id=3)
    assert len(result) == 1
    assert result[0].learner_id == 10


def test_filter_all_interactions_match():
    """All interactions have same item_id."""
    interactions = [
        _make_log(1, 1, 5),
        _make_log(2, 2, 5),
        _make_log(3, 3, 5),
    ]
    result = _filter_by_item_id(interactions, item_id=5)
    assert len(result) == 3


def test_filter_by_item_id_zero():
    """Filter with item_id=0."""
    interactions = [_make_log(1, 1, 0), _make_log(2, 2, 5)]
    result = _filter_by_item_id(interactions, item_id=0)
    assert len(result) == 1
    assert result[0].id == 1