import pytest

from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith

from app.main import calculate_team_total_rating, elves_concert, feast_of_the_dwarves


def test_elf_ranger():
    ranger = ElfRanger(nickname="Nardual Chaekian", musical_instrument="flute", bow_level=7)
    assert ranger.get_rating() == 21
    assert ranger.player_info() == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"


def test_druid():
    druid = Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC")
    assert druid.get_rating() == 3
    assert druid.player_info() == "Druid Druid. Druid has a favourite spell: ABC"


def test_dwarf_warrior():
    warrior = DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=7)
    assert warrior.get_rating() == 11
    assert warrior.player_info() == "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"


def test_dwarf_blacksmith():
    blacksmith = DwarfBlacksmith(nickname="Smith", favourite_dish="Steak", skill_level=5)
    assert blacksmith.get_rating() == 5
    assert blacksmith.player_info() == "Dwarf blacksmith Smith with skill of the 5 level"


def test_calculate_team_total_rating():
    team = [
        Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
        ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
    ]
    assert calculate_team_total_rating(team) == 102  # 33*3 + 3


def test_elves_concert(capsys):
    elves = [
        Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
    ]
    elves_concert(elves)
    captured = capsys.readouterr()
    assert "Nardual is playing a song on the flute" in captured.out
    assert "Rothilion is playing a song on the trumpet" in captured.out


def test_feast_of_the_dwarves(capsys):
    dwarves = [
        DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
        DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
    ]
    feast_of_the_dwarves(dwarves)
    captured = capsys.readouterr()
    assert "Thiddeal is eating French Fries" in captured.out
    assert "Dwarf is eating Caesar Salad" in captured.out
