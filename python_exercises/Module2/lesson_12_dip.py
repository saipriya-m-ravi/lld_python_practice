"""
Lesson 2.5 - Dependency Inversion Principle (DIP)

Step 1: Read BadOverdueReportService below. Notice it directly creates
        a MySQLMemberRepository inside its own __init__ -- a high-level
        class (report generation) hardwired to a low-level detail
        (a specific database).
Step 2: Think through why this makes testing painful: how would you
        test the report-formatting logic WITHOUT hitting a real
        (or heavily faked) MySQL connection, given the current design?
Step 3: Refactor so OverdueReportService depends on an abstraction,
        not a concrete database class -- then prove it by running the
        SAME service with two different injected repositories: a real
        one and a fake in-memory one for testing.
"""

from abc import ABC, abstractmethod


class MemberRepository(ABC):
    @abstractmethod
    def get_overdue_members(self):
        pass
    
    
class MySQLMemberRepository(MemberRepository):
    def get_overdue_members(self):
        print("Querying MySQL for overdue members...")
        return ["Alice", "Bob"]


class InMemoryMemberRepository(MemberRepository):
    def get_overdue_members(self):
        print("Querying in memory DB")
        return ["member1", "member2"]
    
    
class OverdueReportService:
    def __init__(self, repo: MemberRepository):
        self.repository = repo
    
    def generate_report(self):
        members = self.repository.get_overdue_members()
        print("Overdue Report:")
        for m in members:
            print(f" - {m}")
            
            
class BadOverdueReportService:
    def __init__(self):
        self.repository = MySQLMemberRepository()   # hardcoded low-level dependency

    def generate_report(self):
        members = self.repository.get_overdue_members()
        print("Overdue Report:")
        for m in members:
            print(f" - {m}")


# ============================================================
# TODO: Refactor.
#
# 1. Define an abstract MemberRepository(ABC) with an abstract method
#    get_overdue_members().
# 2. Make MySQLMemberRepository implement MemberRepository.
# 3. Rewrite OverdueReportService to accept a MemberRepository via its
#    __init__ parameter, instead of constructing one itself.
# 4. Write a second implementation, InMemoryMemberRepository, that
#    just returns a hardcoded list -- no "database" involved at all.
#    This is what you'd use in a real unit test, to test
#    OverdueReportService's report-FORMATTING logic in complete
#    isolation from any real database.
# 5. In __main__, run OverdueReportService twice: once injected with
#    MySQLMemberRepository(), once with InMemoryMemberRepository() --
#    same service class, zero code changes to OverdueReportService
#    itself between the two runs.
# ============================================================


if __name__ == "__main__":
    ors1 = OverdueReportService(MySQLMemberRepository())
    ors2 = OverdueReportService(InMemoryMemberRepository())
    
    ors1.generate_report()
    ors2.generate_report()
