import game_configs
from models.base import Base
from sqlalchemy import TEXT, Boolean, Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class GamePvE(Base):
    __tablename__ = "game_pve"
    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(DateTime)
    # 一些在比赛结束后保存的字段
    name = Column(String(1000))
    type = Column(String(1000))
    date = Column(String(1000))
    season = Column(Integer)

    save_id = Column(Integer, ForeignKey("save.id"))
    player_club_id = Column(Integer, ForeignKey("club.id"))
    computer_club_id = Column(Integer, ForeignKey("club.id"))

    home_club_id = Column(Integer)

    turns = Column(Integer)
    cur_attacker = Column(Integer)
    script = Column(TEXT)
    new_script = Column(TEXT)
    counter_attack_permitted = Column(Boolean, default=False)
    is_extra_time = Column(Boolean, default=False)
    goal_record = Column(String(1000))

    teams = relationship("TeamPvE", backref="game_pve", cascade="all, delete-orphan")


class TeamPvE(Base):
    __tablename__ = "team_pve"
    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(DateTime)
    is_player = Column(Boolean, default=False)

    club_id = Column(Integer, ForeignKey("club.id"))
    score = Column(Integer)

    attempts = Column(Integer)
    # 下底传中
    wing_cross = Column(Integer)
    wing_cross_success = Column(Integer)
    # 内切
    under_cutting = Column(Integer)
    under_cutting_success = Column(Integer)
    # 倒三角
    pull_back = Column(Integer)
    pull_back_success = Column(Integer)
    # 中路渗透
    middle_attack = Column(Integer)
    middle_attack_success = Column(Integer)
    # 防反
    counter_attack = Column(Integer)
    counter_attack_success = Column(Integer)

    game_pve_id = Column(Integer, ForeignKey("game_pve.id"))
    players = relationship("PlayerPvE", backref="team_pve", cascade="all, delete-orphan")


class PlayerPvE(Base):
    __tablename__ = "player_pve"
    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(DateTime)

    player_id = Column(Integer)
    ori_location = Column(Enum(game_configs.Location))
    real_location = Column(Enum(game_configs.Location))

    real_rating = Column(Float)
    final_rating = Column(Float)
    actions = Column(Integer)
    shots = Column(Integer)
    goals = Column(Integer)
    assists = Column(Integer)
    # 传球
    passes = Column(Integer)
    pass_success = Column(Integer)
    # 过人
    dribbles = Column(Integer)
    dribble_success = Column(Integer)
    # 抢断
    tackles = Column(Integer)
    tackle_success = Column(Integer)
    # 争顶
    aerials = Column(Integer)
    aerial_success = Column(Integer)
    # 扑救
    saves = Column(Integer)
    save_success = Column(Integer)
    # 体力
    original_stamina = Column(Integer)
    final_stamina = Column(Integer)

    team_pve_id = Column(Integer, ForeignKey("team_pve.id"))
