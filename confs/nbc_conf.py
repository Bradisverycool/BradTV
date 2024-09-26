station_conf = {
    # basic human readable name for the channel
    'network_name' : "NBC",
    # path to the catalog binary file to be stored
    'catalog_path' : "catalog/nbc_catalog.bin",
    # root directory for content for this station
    'content_dir' : "catalog/nbc_catalog",
    # runtime dir for this station - where schedules etc will be stored
    'runtime_dir' : "runtime/nbc",
    # path to output the weekly schedule
    'schedule_path': "runtime/nbc_schedule.bin",
    # must be inside or linked inside content_dir
    'commercial_dir' : "commercial",
    # must be inside or linked inside content_dir
    'bump_dir' : "bump",
    # list of directories (tags) intended to be stitched clips vs full content in a single file
    'clip_shows' : ["real_people", "snl"],

    #used at sign-off time (played once)
    'sign_off_video': "catalog/anthem_signoff.mp4",
    #used when the channel is offair
    'off_air_video': "catalog/off_air_pattern.mp4",

    'monday': {
        #will play random content from the content/morning path
        7: {'tags': 'morning'},
        #will play random content from the content/morning path
        8: {'tags': 'morning'},
        #will play random content from the content/cartoon path
        9: {'tags': 'cartoon'},
        #will play random content from the content/gameshow path
        10: {'tags' : 'gameshow'},
        11: {'tags' : 'gameshow'},
        12: {'tags' : 'daytime'},
        13: {'tags' : 'daytime'},
        14: {'tags' : 'daytime'},
        15: {'tags' : 'classic'},
        16: {'tags' : 'syndication'},
        17: {'tags' : 'syndication'},
        18: {'tags' : 'news'},
        19: {'tags' : 'gameshow'},
        20: {'tags' : 'sitcom'},
        21: {'tags' : 'prime'},
        22: {'tags' : 'prime'},
        23: {'tags' : 'news'},
        0: {'tags' : 'late'},
        1: {'tags' : 'late-late'},
        2: {'tags' : 'classic'},
        3: {'event' : 'signoff'}
    },
    'tuesday': {
        7: {'tags': 'morning'},
        8: {'tags': 'morning'},
        9: {'tags': 'cartoon'},
        10: {'tags' : 'gameshow'},
        11: {'tags' : 'gameshow'},
        12: {'tags' : 'daytime'},
        13: {'tags' : 'daytime'},
        14: {'tags' : 'daytime'},
        15: {'tags' : 'classic'},
        16: {'tags' : 'syndication'},
        17: {'tags' : 'syndication'},
        18: {'tags' : 'news'},
        19: {'tags' : 'gameshow'},
        20: {'tags' : 'sitcom'},
        21: {'tags' : 'prime'},
        22: {'tags' : 'prime'},
        23: {'tags' : 'news'},
        0: {'tags' : 'late'},
        1: {'tags' : 'late-late'},
        2: {'tags' : 'classic'},
        3: {'event' : 'signoff'}
    },
    'wednesday': {
        7: {'tags': 'morning'},
        8: {'tags': 'morning'},
        9: {'tags': 'cartoon'},
        10: {'tags' : 'gameshow'},
        11: {'tags' : 'gameshow'},
        12: {'tags' : 'daytime'},
        13: {'tags' : 'daytime'},
        14: {'tags' : 'daytime'},
        15: {'tags' : 'classic'},
        16: {'tags' : 'syndication'},
        17: {'tags' : 'syndication'},
        18: {'tags' : 'news'},
        19: {'tags' : 'gameshow'},
        20: {'tags' : 'real_people'},
        21: {'tags' : 'prime'},
        22: {'tags' : 'prime'},
        23: {'tags' : 'news'},
        0: {'tags' : 'late'},
        1: {'tags' : 'late-late'},
        2: {'tags' : 'classic'},
        3: {'event' : 'signoff'}
    },
    'thursday': {
        7: {'tags': 'morning'},
        8: {'tags': 'morning'},
        9: {'tags': 'cartoon'},
        10: {'tags' : 'gameshow'},
        11: {'tags' : 'gameshow'},
        12: {'tags' : 'daytime'},
        13: {'tags' : 'daytime'},
        14: {'tags' : 'daytime'},
        15: {'tags' : 'classic'},
        16: {'tags' : 'syndication'},
        17: {'tags' : 'syndication'},
        18: {'tags' : 'news'},
        19: {'tags' : 'gameshow'},
        20: {'tags' : 'sitcom'},
        21: {'tags' : 'sitcom'},
        22: {'tags' : 'prime'},
        23: {'tags' : 'news'},
        0: {'tags' : 'late'},
        1: {'tags' : 'late-late'},
        2: {'tags' : 'classic'},
        3: {'event' : 'signoff'}
    },
    'friday': {
        7: {'tags': 'morning'},
        8: {'tags': 'morning'},
        9: {'tags': 'cartoon'},
        10: {'tags' : 'gameshow'},
        11: {'tags' : 'gameshow'},
        12: {'tags' : 'daytime'},
        13: {'tags' : 'daytime'},
        14: {'tags' : 'daytime'},
        15: {'tags' : 'classic'},
        16: {'tags' : 'syndication'},
        17: {'tags' : 'syndication'},
        18: {'tags' : 'news'},
        19: {'tags' : 'gameshow'},
        20: {'tags' : 'sitcom'},
        21: {'tags' : 'sitcom'},
        22: {'tags' : 'prime'},
        23: {'tags' : 'news'},
        0: {'tags' : 'late'},
        1: {'tags' : 'late-late'},
        2: {'tags' : 'classic'},
        3: {'event' : 'signoff'}
    },
    'saturday': {
        7: {'tags': 'cartoon'},
        8: {'tags': 'cartoon'},
        9: {'tags': 'cartoon'},
        10: {'tags' : 'cartoon'},
        11: {'tags' : 'cartoon'},
        12: {'tags' : 'cartoon'},
        13: {'tags' : 'wrestling'},
        14: {'tags' : 'wrestling'},
        15: {'tags' : 'classic'},
        16: {'tags' : 'syndication'},
        17: {'tags' : 'syndication'},
        18: {'tags' : 'news'},
        19: {'tags' : 'gameshow'},
        20: {'tags' : 'sitcom'},
        21: {'tags' : 'sitcom'},
        22: {'tags' : 'prime'},
        23: {'tags' : 'news'},
        0: {'tags' : 'snl'},
        1: {'tags' : 'snl'},
        2: {'tags' : 'classic'},
        3: {'event' : 'signoff'}
    },
    'sunday': {
        7: {'tags': 'cartoon'},
        8: {'tags': 'cartoon'},
        9: {'tags': 'classic'},
        10: {'tags' : 'sunday'},
        11: {'tags' : 'sunday'},
        12: {'tags' : 'sunday'},
        13: {'tags' : 'western'},
        14: {'tags' : 'western'},
        15: {'tags' : 'western'},
        16: {'tags' : 'wrestling'},
        17: {'tags' : 'syndication'},
        18: {'tags' : 'news'},
        19: {'tags' : 'gameshow'},
        20: {'tags' : 'sitcom'},
        21: {'tags' : 'real_people'},
        22: {'tags' : 'prime'},
        23: {'tags' : 'prime'},
        0: {'tags' : 'classic'},
        1: {'tags' : 'classic'},
        2: {'tags' : 'classic'},
        3: {'event' : 'signoff'}
    }
}
