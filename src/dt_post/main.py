from lib.suite_loaders import load_from_json_files


def main() -> None:

    suite = load_from_json_files("suite.json", "suite_env.json")

    suite.run()

    # print(suite.vars)
