from invoke import task

@task
def start(ctx):
  ctx.run("python3 src/solver.py")

@task
def test(ctx):
  ctx.run("pytest src")

@task
def lint(ctx):
  ctx.run("pylint src")