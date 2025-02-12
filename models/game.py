from game_configs.game_config import Location
from models.base import Base
from sqlalchemy import TEXT, Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


# region 比赛输出数据
class Game(Base):
    __tablename__ = "game"
    id = Column(Integer, primary_key=True, index=True)

    created_time = Column(DateTime)
    name = Column(String(1000))
    type = Column(String(1000))
    date = Column(String(1000))
    season = Column(String(1000))
    script = Column(TEXT)
    goal_record = Column(String(2000))

    teams = relationship("GameTeamInfo", backref="game")
    save_id = Column(Integer)

    mvp = Column(Integer)
    winner_id = Column(Integer)


class GameTeamInfo(Base):
    __tablename__ = "game_team_info"
    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("game.id"))  # 外键
    club_id = Column(Integer, ForeignKey("club.id"))  # 与俱乐部类连接的外键

    season = Column(Integer)
    created_time = Column(DateTime)
    score = Column(Integer)
    team_data = relationship("GameTeamData", uselist=False, backref="game_team_info")
    player_data = relationship("GamePlayerData", backref="game_team_info")


class GameTeamData(Base):
    __tablename__ = "game_team_data"
    id = Column(Integer, primary_key=True, index=True)
    game_team_info_id = Column(Integer, ForeignKey("game_team_info.id"))

    season = Column(Integer)
    created_time = Column(DateTime)
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


class GamePlayerData(Base):
    # 球员的一场比赛数据
    __tablename__ = "game_player_data"
    id = Column(Integer, primary_key=True, index=True)

    season = Column(Integer)
    created_time = Column(DateTime)
    location = Column(Enum(Location))

    real_rating = Column(Float)  # 未截取最大值的真实评分
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

    game_team_info_id = Column(Integer, ForeignKey("game_team_info.id"))
    player_id = Column("player_id", Integer, ForeignKey("player.id"), index=True)


# endregion
