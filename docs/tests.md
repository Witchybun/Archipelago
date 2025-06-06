# Archipelago Unit Testing API

This document covers some of the generic tests available using Archipelago's unit testing system, as well as some basic
steps on how to write your own.

## Generic Tests

Some generic tests are run on every World to ensure basic functionality with default options. These basic tests can be
found in the [general test directory](/test/general).

## Defining World Tests

In order to run tests from your world, you will need to create a `test` package within your world package. This can be
done by creating a `test` directory inside your world with an (empty) `__init__.py` inside it. By convention, a base
for your world tests can be created in `bases.py` or any file that does not start with `test`, that you can then import
into other modules. All tests should be defined in files named `test_*.py` (all lower case) and be member functions
(named `test_*`) of classes (named `Test*` or `*Test`) that inherit from `unittest.TestCase` or a test base.

Defining anything inside `test/__init__.py` is deprecated. Defining TestBase there was previously the norm; however,
it complicates test discovery because some worlds also put actual tests into `__init__.py`.

### WorldTestBase

In order to test basic functionality of varying options, as well as to test specific edge cases or that certain
interactions in the world interact as expected, you will want to use the [WorldTestBase](/test/bases.py). This class
comes with the basics for test setup as well as a few preloaded tests that most worlds might want to check on varying
options combinations.

Example `/worlds/<my_game>/test/bases.py`:

```python
from test.bases import WorldTestBase


class MyGameTestBase(WorldTestBase):
    game = "My Game"
```

The basic tests that WorldTestBase comes with include `test_all_state_can_reach_everything`,
`test_empty_state_can_reach_something`, and `test_fill`. These test that with all collected items everything is
reachable, with no collected items at least something is reachable, and that a valid multiworld can be completed with
all steps being called, respectively.

### Writing Tests

#### Using WorldTestBase

Adding runs for the basic tests for a different option combination is as easy as making a new module in the test
package, creating a class that inherits from your game's TestBase, and defining the options in a dict as a field on the
class. The new module should be named `test_<something>.py` and have at least one class inheriting from the base, or
define its own testing methods. Newly defined test methods should follow standard PEP8 snake_case format and also start
with `test_`.

Example `/worlds/<my_game>/test/test_chest_access.py`:

```python
from .bases import MyGameTestBase


class TestChestAccess(MyGameTestBase):
    options = {
        "difficulty": "easy",
        "final_boss_hp": 4000,
    }

    def test_sword_chests(self) -> None:
        """Test locations that require a sword"""
        locations = ["Chest1", "Chest2"]
        items = [["Sword"]]
        # This tests that the provided locations aren't accessible without the provided items, but can be accessed once
        # the items are obtained.
        # This will also check that any locations not provided don't have the same dependency requirement.
        # Optionally, passing only_check_listed=True to the method will only check the locations provided.
        self.assertAccessDependency(locations, items)
```

When tests are run, this class will create a multiworld with a single player having the provided options, and run the
generic tests, as well as the new custom test. Each test method definition will create its own separate solo multiworld
that will be cleaned up after. If you don't want to run the generic tests on a base, `run_default_tests` can be
overridden. For more information on what methods are available to your class, check the
[WorldTestBase definition](/test/bases.py#L106).

#### Alternatives to WorldTestBase

Unit tests can also be created using [TestBase](/test/bases.py#L16) or
[unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase) depending on your use case. These
may be useful for generating a multiworld under very specific constraints without using the generic world setup, or for
testing portions of your code that can be tested without relying on a multiworld to be created first.

#### Parametrization

When defining a test that needs to cover a range of inputs it is useful to parameterize (to run the same test
for multiple inputs) the base test. Some important things to consider when attempting to parametrize your test are:

* [Subtests](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests)
  can be used to have parametrized assertions that show up similar to individual tests but without the overhead
  of needing to instantiate multiple tests; however, subtests can not be multithreaded and do not have individual
  timing data, so they are not suitable for slow tests.

* Archipelago's tests are test-runner-agnostic. That means tests are not allowed to use e.g. `@pytest.mark.parametrize`.
  Instead, we define our own parametrization helpers in [test.param](/test/param.py).

* Classes inheriting from `WorldTestBase`, including those created by the helpers in `test.param`, will run all
  base tests by default, make sure the produced tests actually do what you aim for and do not waste a lot of
  extra CPU time. Consider using `TestBase` or `unittest.TestCase` directly
  or setting `WorldTestBase.run_default_tests` to False.

#### Performance Considerations

Archipelago is big enough that the runtime of unittests can have an impact on productivity.

Individual tests should take less than a second, so they can be properly multithreaded.

Ideally, thorough tests are directed at actual code/functionality. Do not just create and/or fill a ton of individual
Multiworlds that spend most of the test time outside what you actually want to test.

Consider generating/validating "random" games as part of your APWorld release workflow rather than having that be part
of continuous integration, and add minimal reproducers to the "normal" tests for problems that were found.
You can use [@unittest.skipIf](https://docs.python.org/3/library/unittest.html#unittest.skipIf) with an environment
variable to keep all the benefits of the test framework while not running the marked tests by default.

## Running Tests

#### Using Pycharm

In PyCharm, running all tests can be done by right-clicking the root test directory and selecting Run 'Archipelago Unittests'. 
If you have never previously run ModuleUpdate.py, then you will need to do this once before the tests will run. 
You can run ModuleUpdate.py by right-clicking ModuleUpdate.py and selecting `Run 'ModuleUpdate'`. 
After running ModuleUpdate.py you may still get a `ModuleNotFoundError: No module named 'flask'` for the webhost tests. 
If this happens, run WebHost.py by right-clicking it and selecting `Run 'WebHost'`. Make sure to press enter when prompted. 
Unless you configured PyCharm to use pytest as a test runner, you may get import failures. To solve this, 
edit the run configuration, and set the working directory to the Archipelago directory which contains all the project files. 

If you only want to run your world's defined tests, repeat the steps for the test directory within your world.
Your working directory should be the directory of your world in the worlds directory and the script should be the 
tests folder within your world.

You can also find the 'Archipelago Unittests' as an option in the dropdown at the top of the window
next to the run and debug buttons.

#### Running Tests without Pycharm

Run `pip install pytest pytest-subtests`, then use your IDE to run tests or run `pytest` from the source folder.

#### Running Tests Multithreaded

pytest can run multiple test runners in parallel with the pytest-xdist extension.

Install with `pip install pytest-xdist`.

Run with `pytest -n12` to spawn 12 process that each run 1/12th of the tests.
